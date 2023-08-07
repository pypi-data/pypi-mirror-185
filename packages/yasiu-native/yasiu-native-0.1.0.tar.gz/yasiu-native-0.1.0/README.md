# Readme of `yasiu-native`

Module with useful measure time decorators.

## Installation

```shell
pip install yasiu-native
```

## Time decorators

- **measure_perf_time_decorator**

  decorator that measures time using *time.perf_counter*


- **measure_real_time_decorator**

  decorator that measures time using *time.time*

### Measuring time

```py
from yasiu_native.time import measure_perf_time_decorator


@measure_perf_time_decorator()
def func():
    ...


@measure_perf_time_decorator(">4.1f")
def func():
    ...


@measure_perf_time_decorator(fmt=">4.1f")
def func():
    ...
```

### Print buffering will impact your performance!

- Use with cauction for multiple function calls

## Flexible decorator

Decorator that checks if decorated function was passed with `()` or not

```python
from yasiu_native.decorators import flexible_decorator


@flexible_decorator
def custom_decorator(func, decor_variable):
    def wrapper(*a, **kw):
        print(f"Decorated with {decor_variable}")
        return func(*a, **kw)

    return wrapper


@custom_decorator
def test_1():
    pass


@custom_decorator()
def test_2():
    pass


@custom_decorator(a=1)
def test_3(a=0):
    pass

```

## Console execution timer

not here yet.

# All packages

[1. Native Package](https://pypi.org/project/yasiu-time/)

[2. Math Package](https://pypi.org/project/yasiu-math/)

[3. Image Package](https://pypi.org/project/yasiu-image/)

[4. Pyplot visualisation Package](https://pypi.org/project/yasiu-vis/)

