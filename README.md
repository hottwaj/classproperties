# classproperties

Decorators for classproperty and cached_classproperty

Python 3 compatible only.  No dependencies.

## Example usage

```
from classproperties import classproperty, cached_classproperty
class C(object):

    @classproperty
    def x(cls):
        return 1

assert C.x == 1
assert C().x == 1

class CCached(object):

    @cached_classproperty
    def x(cls):
        print('executed only once')
        return 1

assert CCached.x == 1
assert CCached().x == 1
```

## Tests

See tests.py for example usage and expected behaviour

To run tests:

```
python tests.py
```

## Credits

Credits to Denis Ryzhkov on Stackoverflow for the implementation of classproperty:
https://stackoverflow.com/a/13624858/1280629
