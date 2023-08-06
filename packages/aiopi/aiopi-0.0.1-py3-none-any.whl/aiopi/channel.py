import asyncio
import functools
import itertools
import logging
import math
from collections.abc import Awaitable, AsyncIterable, Iterable
from typing import (
    Any,
    Callable,
    List,
    Optional,
    Sequence,
    Set,
    Union
)

from aiohttp import ClientSession, ClientWebSocketResponse
from dints.abc import AbstractClient, AbstractConnection
from dints.models import ErrorMessage
from pendulum.tz.zoneinfo.exceptions import InvalidTimezone
from pydantic import ValidationError

from aiopi.constants import TIMEZONE
from aiopi.models import PIMessage, PISubscription, WebIdType



_LOGGER = logging.getLogger(__name__)


class PIChannelConnection(AbstractConnection):
    """Represents a single websocket connection to a PI Web API streamset endpoint.
    
    `PIChannelConnection` handles the connecting, receiving and parsing of messages
    for a set of PI tags and then passes those messages to the parent client
    object.
    """
    def __init__(
        self,
        client: "PIChannelClient",
        loop: asyncio.AbstractEventLoop,
        *,
        web_id_type: WebIdType,
        max_subscriptions: int,
        max_reconnect_attempts: int,
        backoff_factor: float,
        initial_backoff: float,
        max_backoff: float,
        protocols: Optional[Iterable[str]],
        heartbeat: float,
        close_timeout: float,
        max_msg_size: int,
        timezone: str
    ) -> None:
        super().__init__(client, loop)
        self.web_id_type = web_id_type.value
        self.max_subscriptions = max_subscriptions
        self.max_reconnect_attempts = max_reconnect_attempts
        self.backoff_factor = backoff_factor
        self.initial_backoff = initial_backoff
        self.max_backoff = max_backoff
        self.protocols = protocols
        self.heartbeat = heartbeat
        self.close_timeout = close_timeout
        self.max_msg_size = max_msg_size
        self.timezone = timezone

    @property
    def should_reconnect(self) -> bool:
        """`True` if the client reconnect settings are set else `False`"""
        return (
            self.max_reconnect_attempts is not None and
            self.max_reconnect_attempts > 0
        )

    @property
    def capacity(self) -> int:
        """The number of additional subscriptions this connection can support."""
        return self.max_subscriptions - len(self.subscriptions)

    async def connect(self) -> ClientWebSocketResponse:
        """Attempt to establish a websocket connection to the remote host."""
        return await self.client.session.ws_connect(
            self.build_url(),
            protocols=self.protocols,
            heartbeat=self.heartbeat,
            timeout=self.close_timeout,
            max_msg_size=self.max_msg_size
        )

    async def run(self, ws: ClientWebSocketResponse) -> None:
        """Receive, parse and validate messages from the websocket connection.
        
        Messages are not buffered on the connection if the client is not ready
        to receive messages from the connection, they are thrown away instead.

        If configured, this method will handle reconnecting if the connection to
        the remote host is dropped.
        """
        try:
            while True:
                async for msg in ws:
                    # The client will put the connection `online` when it is ready
                    # to receive messages from it. Otherwise we just throw away
                    # the message
                    if self._online:
                        try:
                            data = PIMessage.parse_raw(msg.data).in_timezone(self.timezone)
                        except ValidationError:
                            _LOGGER.warning("Message validation failed", exc_info=True, extra={"raw": msg.data})
                        except InvalidTimezone:
                            raise
                        except Exception:
                            _LOGGER.error("An unhandled error occurred parsing the message", exc_info=True, extra={"raw": msg.data})
                        else:
                            await self.client._data_queue.put(data.json())
                else:
                    assert ws.closed
                    close_code = ws.close_code
                    _LOGGER.warning(
                        "Websocket closed by peer or network failure %i", close_code
                    )
                    exc = ws.exception()
                    if self.should_reconnect:
                        attempts = 0
                        while attempts < self.max_reconnect_attempts:
                            _LOGGER.info(
                                "Attempting reconnect. Attempt %i of %i",
                                attempts + 1,
                                self.max_reconnect_attempts
                            )
                            try:
                                ws = await self.connect()
                            except Exception:
                                backoff_delay = (
                                    self.initial_backoff * self.backoff_factor ** attempts
                                )
                                backoff_delay = min(
                                    
                                    self.max_backoff,
                                    int(backoff_delay)
                                )
                                _LOGGER.debug(
                                    "Reconnect failed. Trying again in %0.2f seconds",
                                    backoff_delay,
                                    exc_info=True
                                )
                                await asyncio.sleep(backoff_delay)
                                attempts += 1
                            else:
                                break
                        if ws.closed:
                            if exc is not None:
                                raise exc
                            break
                    else:
                        if exc is not None:
                            raise exc
                        break
        finally:
            if not ws.closed:
                await ws.close()
    
    async def start(self, subscriptions: Sequence[PISubscription]) -> Any:
        """Start the websocket connection and background data retrieval task."""
        if self.is_running:
            raise RuntimeError("Attempted to start a running connection")
        
        self.subscriptions.update(subscriptions)
        
        ws = await self.connect()
        
        runner = self._loop.create_task(self.run(ws))
        runner.add_done_callback(self.connection_lost)
        self._runner = runner

    def build_url(self) -> str:
        web_id_type = self.web_id_type
        for subscription in self.subscriptions:
            if subscription.web_id_type != web_id_type:
                raise ValueError(f"Invalid WebIdType for subscription {subscription.web_id}")
        return f"/streamsets/channels?webId={'&webId='.join([subscription.web_id for subscription in self.subscriptions])}&webIdType={web_id_type}"


class PIChannelClient(AbstractClient):
    """Client for streaming data from the PI Web API via websockets."""
    def __init__(
        self,
        session: ClientSession,
        web_id_type: WebIdType = WebIdType.FULL,
        *,
        max_connections: int = 50,
        max_subscriptions: int = 30,
        max_buffered_messages: int = 1000,
        max_reconnect_attempts: int = 5,
        backoff_factor: float = 1.618,
        initial_backoff: float = 5.0,
        max_backoff: float = 60.0,
        protocols: Optional[Iterable[str]] = None,
        heartbeat: float = 20.0,
        close_timeout: float = 10.0,
        max_msg_size: int = 4*1024*1024,
        timezone: str = TIMEZONE
    ) -> None:
        super().__init__()
        self.session = session
        self.web_id_type = web_id_type
        self._max_capacity = max_connections * max_subscriptions
        self._max_subscriptions = max_subscriptions
        
        self._connection_factory: Callable[[], PIChannelConnection] = functools.partial(
            PIChannelConnection,
            self,
            self._loop,
            web_id_type=web_id_type,
            max_subscriptions=max_subscriptions,
            max_reconnect_attempts=max_reconnect_attempts,
            backoff_factor=backoff_factor,
            initial_backoff=initial_backoff,
            max_backoff=max_backoff,
            protocols=protocols,
            heartbeat=heartbeat,
            close_timeout=close_timeout,
            max_msg_size=max_msg_size,
            timezone=timezone
        )
        self._consolidate_task: asyncio.Task = None
        self._data_queue: asyncio.Queue = asyncio.Queue(max_buffered_messages)
        self._subscription_event: asyncio.Event = asyncio.Event()
        self._subscription_lock: asyncio.Lock = asyncio.Lock()
    
    @property
    def capacity(self) -> int:
        """The number of additional PI tag subscriptions the client can support."""
        return self._max_capacity - len(self.subscriptions)

    def connection_lost(self, connection: "PIChannelConnection") -> None:
        """Callback for `PIChannelConnection` indicating the connection has been lost."""
        exc = connection.exception
        if exc is not None:
            self._errors_queue.put_nowait(
                ErrorMessage(
                    exc=exc,
                    subscriptions=connection.subscriptions
                )
            )
        if connection in self._connections:
            self._connections.remove(connection)

    async def close(self) -> None:
        """Cancel the consolidation task, stop all connection workers and close
        the unerlying session.
        """
        task = self._consolidate_task
        self._consolidate_task = None
        if task is not None:
            task.cancel()
        for connection in self._connections: connection.stop()
        self._connections.clear()
        await self.session.close()

    async def messages(self) -> AsyncIterable[str]:
        """Receive incoming messages for all PI tag subscriptions.
        
        Yields:
            message: The result of `PIMessage.json()`
        """
        while True:
            msg = await self._data_queue.get()
            yield msg

    async def errors(self) -> AsyncIterable[ErrorMessage]:
        """Receive errors that cause connections to fail.
        
        Yields:
            error: An instance of `ErrorMessage`
        """
        while True:
            err = await self._errors_queue.get()
            yield err

    async def subscribe(self, subscriptions: Sequence[PISubscription]) -> bool:
        """Subscribe the client to a sequence of PI tags.
        
        This method will open the necessary connections to support all the subscriptions.
        However, if the number of subscriptions would cause the client to exceed
        the `max_connections` specified, nothing will be done.
        
        Additionally, the subscription process is an all or nothing process. If
        one connection required to support a subset of the total number of subscriptions
        does not start properly then all other connections supporting the remaining
        subscriptions will also be stopped.

        Args:
            subscriptions: The sequence of subscriptions to subscribe to

        Returns:
            result: A boolean indicating the success of the operation. `True` means
                that all subscriptions were successfully subscribed to. `False` means
                that none of the subscriptions were subscribed to
        """
        subscriptions: Set[PISubscription] = set(subscriptions)
        self._start_consolidation()
        
        async with self._subscription_lock:
            existing = self.subscriptions
            capacity = self.capacity
            subscriptions = list(subscriptions.difference(existing))
            count = len(subscriptions)
            
            if subscriptions and capacity > count:
                conns = await self._create_connections(subscriptions)
                if not all([conn.is_running for conn in conns]):
                    return False
                for conn in conns: conn.toggle()
                self._connections.extend(conns)
                self._subscription_event.set()
                _LOGGER.debug("Subscribed to %i WebId's", count)
            
            elif subscriptions and capacity < count:
                return False

            return True

    async def unsubscribe(self, subscriptions: Sequence[PISubscription]) -> bool:
        """Unsubscribe the client from a sequence of subscriptions.

        This is done without disrupting service for other subscriptions. The client
        will scan all active connections for the PI tags specified. It will then
        create new connections to support the remaining subscriptions on those
        exisiting connections. If the new connections start properly, the existing
        ones will be stopped and the this method will return `True`. If the new
        connections do not start properly, the existing connections will continue
        to operate as they did. In that case, this method will return `False`.
        
        Args:
            subscriptions: The sequence of subscriptions to unsubscribe to.

        Returns:
            result: A boolean indicating the success of the operation. `True` means
                that all subscriptions were successfully unsubscribed from. `False` means
                that none of the subscriptions were unsubscribed from.
        """
        subscriptions: Set[PISubscription] = set(subscriptions)
        self._start_consolidation()

        async with self._subscription_lock:
            existing = self.subscriptions
            dne = subscriptions.difference(existing)
            subscriptions = subscriptions.difference(dne)
            
            if subscriptions:
                # Determine the subscriptions we need to keep from existing
                # connections
                keep: List[PISubscription] = []
                old: List[PIChannelConnection] = []
                for connection in self._connections:
                    if len(connection.subscriptions.difference(subscriptions)) != len(connection.subscriptions):
                        old.append(connection)
                        keep.extend(connection.subscriptions.difference(subscriptions))
                
                new: List[PIChannelConnection] = []
                if keep:
                    new = await self._create_connections(keep)
                if not all([connection.is_running for connection in new]):
                    return False
                
                self._transfer_connections(old, new)
                self._connections.extend(new)
                self._subscription_event.set()
                _LOGGER.debug("Unsubscribed from %i WebId's", len(subscriptions))

            return True

    async def _create_connections(self, subs: List[str]) -> List["PIChannelConnection"]:
        """Given a list of subscriptions, open a suitable number of connections
        to support all subscriptions and start the connection workers.
        
        If any worker fails to start, stop all other workers created to support
        the other subscriptions.
        """
        connections: List[PIChannelConnection] = []
        starters: List[Awaitable[None]] = []
        
        while True:
            if len(subs) <= self._max_subscriptions: # This connection will cover the remaining
                connection = self._connection_factory()
                starters.append(connection.start(subs))
                connections.append(connection)
                break
            
            else: # More channels are required
                connection = self._connection_factory()
                starters.append(connection.start(subs[:self._max_subscriptions]))
                connections.append(connection)
                del subs[:self._max_subscriptions]

        errs: List[Union[None, BaseException]] = await asyncio.gather(
            *starters, return_exceptions=True
        )
        
        if not all([err is None for err in errs]):
            for err in errs:
                if err is not None:
                    _LOGGER.warning("Failed to start connection", exc_info=err)
            for connection in connections:
                connection.stop()
        
        else:
            assert all([connection.is_running for connection in connections])
            _LOGGER.debug("Created %i connections", len(connections))
        
        return connections

    async def _run_consolidation(self) -> None:
        """Background task which handles consolidating connection workers which
        are not at capacity.

        Each worker can support `max_subscriptions` subscriptions but the `subscribe`
        method only ever creates new connections. This can lead to multiple
        workers not being at capacity. This task effectively merges subscriptions
        of multiple connections into a smaller number of connections so that each
        connection is supporting `max_subscriptions`. This is guarenteed to not lead
        to a drop in subscriptions as the consolidation process will create new
        workers and only stop the existing ones once all workers have properly
        started.
        """
        while True:
            await self._subscription_event.wait()
            await asyncio.sleep(5)
            
            async with self._subscription_lock:
                try:
                    _LOGGER.debug("Scanning connections for consolidation")
                    available = [
                        connection for connection in self._connections
                        if len(connection.subscriptions) < self._max_subscriptions
                    ]
                    capacity = sum(
                        [
                            len(connection.subscriptions) for connection
                            in available
                        ]
                    )
                    ideal = math.ceil(capacity/self._max_subscriptions)
                    _LOGGER.debug("Ideal number of connections is %i. Total available is %i", ideal, len(available))
                    
                    if ideal == len(available):
                        continue
                    
                    subs = []
                    for connection in available:
                        subs.extend(connection.subscriptions)
                    
                    new = await self._create_connections(subs)
                    if not all([connection.is_running for connection in new]):
                        _LOGGER.warning(
                            "Failed to consolidate channels. One or more new "
                            "channels failed to start"
                        )
                    else:
                        self._transfer_connections(available, new)
                        self._connections.extend(new)
                        _LOGGER.debug("Consolidated %i connections", len(available)-len(new))
                
                finally:
                    self._subscription_event.clear()

    def _start_consolidation(self) -> None:
        """Start the consolidation task if it has not been started or ended unexpectedly."""
        if self._consolidate_task is None or self._consolidate_task.done():
            task = self._loop.create_task(self._run_consolidation())
            self._consolidate_task = task

    def _transfer_connections(
        self,
        old: List[PIChannelConnection],
        new: List[PIChannelConnection]
    ) -> None:
        """Stop existing connections and bring new connections online.
        
        This allows us to atomically swap message processing between connections with
        overlapped subscriptions to ensure duplicate messages are not passed to
        the client.
        """
        for stop, start in itertools.zip_longest(old, new):
            assert stop in self._connections
            assert stop._online
            stop.toggle()
            stop.stop()
            if start is not None:
                start.toggle()