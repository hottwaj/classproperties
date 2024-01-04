from typing import Any, Callable, Generic, TypeVar

T = TypeVar('T')

class classproperty(property, Generic[T]):
    def __init__(self, func: Callable[[Any], T]) -> None: ...
    def __get__(self, owner_self: object, owner_cls: type | None = ...) -> T: ...
