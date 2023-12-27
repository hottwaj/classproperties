from typing import TypeVar, Generic
from functools import cached_property

T: TypeVar = TypeVar('T')


class classproperty(property, Generic[T]):
    """
    Decorator for a Class-level property.

    Credit to Denis Rhyzhkov on Stackoverflow: https://stackoverflow.com/a/13624858/1280629
    """
    
    def __init__(self, func: Callable[[type[Any]], T]) -> None:
        super().__init__(func)

    def __get__(self, owner_self: Any | None, owner_cls: type[Any]) -> T:
        return self.fget(owner_cls)


class cached_classproperty(cached_property):  # n.b. inherits lock and __set_name__ logic from functools.cached_property
    """
    Decorator for a Class-level property whose results are cached.
        e.g.
    class MyClass:
        @cached_classproperty
        def some_complex_calculation(cls):
            return 1000

    Property function is executed once, on first access to the property, and the returned value is stored directly on the class thereafter

    To remove a cached value generated by a cached_classproperty use the classmethod:
    :obj:`cached_classproperty.remove_cached_value`

    i.e. do not use `del MyClass.some_complex_calculation` as this will completely remove the cached value and the
    cached property setter
    """

    def __set_name__(self, cls, name):
        super().__set_name__(cls, name)
        if not hasattr(cls, '_original_cached_classproperties'):
            cls._original_cached_classproperties = {}
        cls._original_cached_classproperties[self.attrname] = self

    def __get__(self, instance, cls):
        if self.attrname is None:
            raise TypeError("Cannot use cached_classproperty instance without calling __set_name__ on it.")

        with self.lock:
            # check if another thread filled cache while we awaited lock
            attrval = cls.__dict__[self.attrname]
            if attrval is self:
                val = self.func(cls)
                setattr(cls, self.attrname, val)  # this overwrites this property on the class
                cls._original_cached_classproperties[self.attrname] = self
            else:
                return attrval
        return val

    @classmethod
    def remove_cached_value(cls, cls_with_cache, name: str):
        """
        This method is provided to enable removing a cached value generated by a cached_classproperty

        If a cached_classproperty is deleted from the parent class e.g. via `del MyClass.some_complex_calculation`,
        then it will be completely removed and subsequently accessing `MyClass.some_complex_calculation`
        will result in an AttributeError, so this method should be used instead.
        """
        if not hasattr(cls_with_cache, '_original_cached_classproperties'):
            raise TypeError(f'{cls_with_cache} has never had any cached_classproperty attributes assigned to it')
        setattr(cls_with_cache, name, cls_with_cache._original_cached_classproperties[name])
