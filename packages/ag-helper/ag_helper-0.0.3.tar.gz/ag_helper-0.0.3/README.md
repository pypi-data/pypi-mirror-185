# ...

## SafeExecutor

The SafeExecutor decorator allows you to quickly execute a function or method within a try/except block.
Parameter ***default*** allows you to override the return value in case of an error. 
Parameter ***logger*** takes a `logger` object and executes the `logger.error(error)` method if an error occurs

### **Examples:**

```

from aghelper.utils import SafeExecutor
from logging import getLogger, StreamHandler, Formatter

logger = getLogger(__name__)
formatter = Formatter("%(asctime)s - %(levelname)s -  %(message)s")

sh = StreamHandler()
sh.setFormatter(formatter)
logger.addHandler(sh)

@SafeExecutor
def foo():
    return 1/0

class FooClass:

    @SafeExecutor
    def foo_method(self):
        return 1/0

    @classmethod
    @SafeExecutor
    def foo_classmethod(cls):
        return 1/0

    @staticmethod
    @SafeExecutor
    def foo_staticmethod():
        return 1/0

    @SafeExecutor(default=0)
    def change_return(self):
        return 1/0

    @SafeExecutor(logger=logger)
    def write_to_log(self):
        return 1/0

print(f"1. Func result: {foo()}")
print(f"2. Method foo result: {FooClass().foo_method()}")
print(f"3. Class method foo result: {FooClass.foo_classmethod()}")
print(f"5. Static method foo result: {FooClass.foo_staticmethod()}")
print(f"6. Set default return: {FooClass().change_return()}")
print(f"7. Write error to log: {FooClass().write_to_log()}")

>>> 1. Func result: None
>>> 2. Method foo result: None
>>> 3. Class method foo result: None
>>> 5. Static method foo result: None
>>> 6. Set default return: 0
>>> 7. Write error to log: None
>>> 2023-01-13 17:06:55,437 - ERROR -  Execute error: division by zero
```