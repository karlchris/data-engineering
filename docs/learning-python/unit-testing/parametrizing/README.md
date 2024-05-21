## Parametrization

**Test parametrization** is a feature in pytest that allows us to write a single test function and test it with multiple input values.
It is a way of writing concise tests that can cover many cases with minimal code.

This feature is especially useful when we want to test a function with varying input parameters.

The main benefit of this is concise code.

```python title="main.py"
def multiply(x, y):
    return x * y
```

```python title="test_file.py"
import pytest
from main import multiply

@pytest.mark.parametrize("x, y, result", [
    (2, 3, 6),
    (1, 1, 1),
    (0, 5, 0),
    (-2, 3, -6),
])
def test_multiply(x, y, result):
    assert multiply(x, y) == result
```

Given you an example to test Python class in [main.py](main.py).

- run command

```bash
docker build -t pytest-parametrizing docs/learning-python/unit-testing/parametrizing/ && docker run pytest-parametrizing
```

## Result

```bash
============================= test session starts ==============================
platform linux -- Python 3.9.19, pytest-8.2.0, pluggy-1.5.0
rootdir: /test
collected 4 items

test_file.py ....                                                        [100%]

============================== 4 passed in 0.01s ===============================
```
