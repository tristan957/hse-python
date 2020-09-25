from enum import Enum
from types import TracebackType
from typing import Dict, Iterator, List, Optional, Tuple, Type, Any


KVDB_VERSION_STRING: str
KVDB_VERSION_TAG: str
KVDB_VERSION_SHA: str


class KvdbException(Exception):
    returncode: int

    def __init__(self, returncode: int) -> KvdbException:
        ...


class Kvdb:
    def close(self) -> None:
        ...

    @staticmethod
    def init() -> None:
        ...

    @staticmethod
    def fini() -> None:
        ...

    @staticmethod
    def make(mp_name: str, params: Optional[Params]=...) -> None:
        ...

    @staticmethod
    def open(mp_name: str, params: Optional[Params]=...) -> Kvdb:
        ...

    def get_names(self) -> List[str]:
        ...

    def kvs_make(self, kvs_name: str, params: Optional[Params]=...) -> None:
        ...

    def kvs_drop(self, kvs_name: str) -> None:
        ...

    def kvs_open(self, kvs_name: str, params: Optional[Params]=...) -> Kvs:
        ...

    def sync(self) -> None:
        ...

    def flush(self) -> None:
        ...

    def compact(self, cancel: bool=..., samp_lwm: bool=...) -> None:
        ...

    def txn_alloc(self) -> KvdbTxn:
        ...


class Kvs:
    def close(self) -> None:
        ...

    def put(self, key: bytes, val: Optional[bytes], priority: bool=..., txn: Optional[KvdbTxn]=...) -> None:
        ...

    def get(self, key: bytes, txn: Optional[KvdbTxn]=..., buf: bytes=...) -> Optional[bytes]:
        ...

    def delete(self, key: bytes, priority: bool=..., txn: Optional[KvdbTxn]=...) -> None:
        ...

    def prefix_delete(self, filt: bytes, priority: bool=..., txn: Optional[KvdbTxn]=...) -> None:
        ...

    def cursor_create(self, filt: Optional[bytes]=..., reverse: bool=..., static_view: bool=..., bind_txn: bool=..., txn: Optional[KvdbTxn]=...) -> KvsCursor:
        ...


class KvdbTxnState(Enum):
    INVALID: int
    ACTIVE: int
    COMMITTED: int
    ABORTED: int


class KvdbTxn:
    def __enter__(self) -> KvdbTxn:
        ...

    def __exit__(self, exc_type: Optional[Type[Exception]], exc_val: Optional[Any], exc_tb: Optional[TracebackType]) -> None:
        ...

    def begin(self) -> None:
        ...

    def commit(self) -> None:
        ...

    def abort(self) -> None:
        ...

    def get_state(self) -> KvdbTxnState:
        ...


class KvsCursor:
    def __enter__(self) -> KvsCursor:
        ...

    def __exit__(self, exc_type: Optional[Type[Exception]], exc_val: Optional[Any], exc_tb: Optional[TracebackType]) -> None:
        ...

    def destroy(self) -> None:
        ...

    def items(self, max_count: Optional[int]=...) -> Iterator[Tuple[bytes, Optional[bytes]]]:
        ...

    def update(self, reverse: Optional[bool]=..., static_view: Optional[bool]=..., bind_txn: Optional[bool]=..., txn: Optional[KvdbTxn]=...) -> None:
        ...

    def seek(self, key: bytes) -> Optional[bytes]:
        ...

    def seek_range(self, filt_min: bytes, filt_max: bytes) -> Optional[bytes]:
        ...

    def read(self) -> Tuple[bytes, bytes, bool]:
        ...


class Params:
    def __getitem__(self, key: str) -> Optional[str]:
        ...

    def __setitem__(self, key:str, value: str) -> None:
        ...

    def get(self, key: str) -> None:
        ...

    def set(self, key: str, value: str) -> None:
        ...

    @staticmethod
    def create() -> Params:
        ...

    @staticmethod
    def from_dict(params: Dict[str, str]) -> Params:
        ...

    @staticmethod
    def from_file(path: str) -> Params:
        ...

    @staticmethod
    def from_string(input: str) -> Params:
        ...
