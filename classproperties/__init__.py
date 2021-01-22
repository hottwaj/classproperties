class classproperty:
    """Decorator for a Class-level property.  Credit to Denis Rhyzhkov on Stackoverflow: https://stackoverflow.com/a/13624858/1280629"""
    def __init__(self, fget, cached=False):
        self.fget = fget
        self.cached=cached

    def __get__(self, owner_self, owner_cls):
        val = self.fget(owner_cls)
        if self.cached:
            setattr(owner_cls, self.fget.__name__, val)
        return val


class cached_classproperty:
    """Decorator for a Class-level property whose results are cached.
    e.g.
class MyClass:
    @cached_classproperty
    def some_complex_calculation(cls):
        return 1000

Property function is executed once, on first access to the property, and the returned value is stored directly on the class thereafter
"""
 
    def __init__(self, fget):
        self.fget = fget
 
    def __get__(self, owner_self, owner_cls):
        val = self.fget(owner_cls)
        setattr(owner_cls, self.fget.__name__, val)
        return val

