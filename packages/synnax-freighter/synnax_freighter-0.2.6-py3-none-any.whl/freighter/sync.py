#  Copyright 2023 Synnax Labs, Inc.
#
#  Use of this software is governed by the Business Source License included in the file
#  licenses/BSL.txt.
#
#  As of the Change Date specified in that file, in accordance with the Business Source
#  License, use of this software will be governed by the Apache License, Version 2.0,
#  included in the file licenses/APL.txt.
#
#  Use of this software is governed by the Business Source License included in the file
#  licenses/BSL.txt.
#
#  As of the Change Date specified in that file, in accordance with the Business Source
#  License, use of this software will be governed by the Apache License, Version 2.0,
#  included in the file licenses/APL.txt.

import asyncio
import contextlib
from asyncio import events
from threading import Thread
from typing import AsyncIterator, Generic, Optional, Type
from xmlrpc.client import boolean

from freighter.metadata import MetaData
from freighter.util.asyncio import cancel_all_tasks
from janus import Queue

from .stream import (
    AsyncStreamClient,
    AsyncStreamReceiver,
    AsyncStreamSenderCloser,
    AsyncStream,
)
from .transport import RQ, RS, P, MiddlewareCollector, AsyncNext
from .util.threading import Notification


@contextlib.asynccontextmanager
async def process(queue: Queue) -> AsyncIterator[P]:
    pld = await queue.async_q.get()
    try:
        yield pld
    finally:
        queue.async_q.task_done()


class _Receiver(Generic[RS]):
    _internal: AsyncStreamReceiver[RS]
    _responses: Queue[tuple[RS | None, Exception | None]]
    _exc: Exception | None

    def __init__(self, internal: AsyncStreamReceiver[RS]):
        self._responses = Queue(maxsize=1)
        self._internal = internal
        self._exc = None

    def received(self) -> bool:
        return self._responses.sync_q.qsize() > 0

    def receive(self) -> tuple[RS | None, Exception | None]:
        if self._exc is not None:
            return None, self._exc

        res, self._exc = self._responses.sync_q.get()
        return res, self._exc

    async def run(self):
        try:
            while True:
                pld, exc = await self._internal.receive()
                await self._responses.async_q.put((pld, exc))
                if exc is not None:
                    return
        except Exception as e:
            await self._responses.async_q.put((None, e))
            raise e


class _SenderCloser(Generic[RQ]):
    _internal: AsyncStreamSenderCloser[RQ]
    _requests: Queue[Optional[RQ]]
    _exit: Notification[bool]
    _exception: Notification[tuple[Exception, bool]]

    def __init__(self, internal: AsyncStreamSenderCloser[RQ]):
        self._internal = internal
        self._requests = Queue()
        self._exception = Notification()
        self._exit = Notification()

    def send(self, pld: RQ) -> Exception | None:
        if self._exception.received():
            return self._handle_exception()

        self._requests.sync_q.put(pld)
        self._requests.sync_q.join()
        return None

    def cancel(self):
        if self._exception.received():
            return self._handle_exception()

        self._requests.sync_q.put(None)
        self._exit.notify(False)
        exc, fatal = self._exception.read(block=True)
        assert not fatal and exc is None

    def close_send(self) -> Exception | None:
        if self._exception.received():
            return self._handle_exception()
        self._requests.sync_q.put(None)
        self._exit.notify(True)
        return self._handle_exception(block=True)

    def _handle_exception(self, block: boolean = False) -> Exception | None:
        exc, fatal = self._exception.read(block=block)
        if fatal:
            raise exc
        return exc

    async def run(self):
        try:
            while True:
                async with process(self._requests) as pld:
                    if await self._maybe_exit(pld):
                        return
                    exc = await self._internal.send(pld)
                    if exc is not None:
                        self._exception.notify((exc, False))
                        return

        except Exception as e:
            self._exception.notify((e, True))
            raise e

    async def _maybe_exit(self, pld: RQ | None) -> bool:
        if not self._exit.received() or pld is not None:
            return False
        exc: Exception | None = None
        graceful = self._exit.read()
        if graceful:
            exc = await self._internal.close_send()
        self._exception.notify((exc, False))
        return True


class SyncStream(Thread, Generic[RQ, RS]):
    """An implementation of the Stream protocol that wraps an AsyncStreamClient
    and exposes a synchronous interface.
    """

    _client: AsyncStreamClient
    _target: str
    _open_exception: Optional[Notification[Optional[Exception]]]
    _receiver: _Receiver[RS]
    _sender: _SenderCloser[RQ]
    _response_factory: Type[RS]
    _request_type: Type[RQ]
    _collector: MiddlewareCollector
    _in_md: MetaData
    _internal: Optional[AsyncStream[RQ, RS]]

    def __init__(
        self,
        client: AsyncStreamClient,
        target: str,
        req_t: Type[RQ],
        res_t: Type[RS],
        collector: MiddlewareCollector,
    ) -> None:
        super().__init__()
        self._client = client
        self._target = target
        self._response_factory = res_t
        self._request_type = req_t
        self._open_exception = Notification()
        self._collector = collector
        self._client.use(self._mw)
        self.start()
        self._ack_open()

    async def _mw(self, md: MetaData, _next: AsyncNext):
        md.params.update(self._in_md.params)
        return await _next(md)

    def run(self) -> None:
        loop = events.new_event_loop()
        try:
            events.set_event_loop(loop)

            def finalizer(_: MetaData) -> tuple[MetaData, Exception | None]:
                return loop.run_until_complete(self._connect())

            self._in_md = MetaData("sync_stream", self._target)
            _, exc = self._collector.exec(self._in_md, finalizer)
            if exc is not None:
                self._open_exception.notify(exc)
                return
            loop.run_until_complete(self._run())
        finally:
            try:
                cancel_all_tasks(loop)
                loop.run_until_complete(loop.shutdown_asyncgens())
                loop.run_until_complete(loop.shutdown_default_executor())
            finally:
                events.set_event_loop(None)
                loop.close()

    def received(self) -> bool:
        """Implement the Stream protocol.
        """
        return self._receiver.received()

    def receive(self) -> tuple[RS | None, Exception | None]:
        """Implement the Stream protocol.
        """
        res, exc = self._receiver.receive()
        if exc is not None:
            self._sender.cancel()
        return res, exc

    def send(self, pld: RQ) -> Exception | None:
        """Implement the Stream protocol.
        """
        return self._sender.send(pld)

    def close_send(self) -> Exception | None:
        """Implement the Stream protocol.
        """
        return self._sender.close_send()

    async def _connect(self) -> tuple[MetaData, Exception | None]:
        out_md = MetaData("sync_stream", self._target)
        try:
            self._internal = await self._client.stream(
                self._target,
                self._request_type,
                self._response_factory,
            )
            return out_md, None
        except Exception as e:
            return out_md, e

    async def _run(self):
        self._receiver = _Receiver(self._internal)
        self._sender = _SenderCloser(self._internal)
        self._open_exception.notify(None)
        await asyncio.gather(self._receiver.run(), self._sender.run())

    def _ack_open(self):
        exc = self._open_exception.read(block=True)
        if exc is not None:
            raise exc
        self._open_exception = None


class SyncStreamClient(MiddlewareCollector):
    """A synchronous wrapper around an AsyncStreamClient that allows a caller to
    use an AsyncStream synchronously.
    """

    internal: AsyncStreamClient

    def __init__(self, internal: AsyncStreamClient) -> None:
        super().__init__()
        self.internal = internal

    def stream(
        self, target: str, req_t: Type[RQ], res_t: Type[RS]
    ) -> SyncStream[RQ, RS]:
        """Implement the StreamClient protocol."""
        return SyncStream[RQ, RS](self.internal, target, req_t, res_t, self)
