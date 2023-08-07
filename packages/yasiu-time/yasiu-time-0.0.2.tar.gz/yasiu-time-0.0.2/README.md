# Readme of `yasiu.time`

Module with useful measure time decorators.

## Installation

```shell
pip install yasiu-time
```

## Time decorators

- **measure_perf_time_decorator**

  decorator that measures time using *time.perf_counter*


- **measure_real_time_decorator**

  decorator that measures time using *time.time*

### Import:

```py
from yasiu_time.time import measure_perf_time_decorator
```

### Print buffering will impact your performance!

- Use with cauction for multiple function calls

### Use examples

```py
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

## Console execution timer

not here yet.

# All packages

[1. Time Package](https://pypi.org/project/yasiu-time/)

[2. Math Package](https://pypi.org/project/yasiu-math/)

[3. Image Package](https://pypi.org/project/yasiu-image/)

[4. Pyplot visualisation Package](https://pypi.org/project/yasiu-vis/)

