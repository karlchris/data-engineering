# Pytest - the `assert` statement

The `assert` statement in Python is used for debugging and testing purposes. It allows us to check if a condition is `True`, and if it's not, it will **Raise** an `Exception` called `AssertionError`.
This can be very helpful in writing unit tests to verify if the expected results match the actual results.

```python
assert condition, message
```

## Steps

- go to [addition.py](addition.py) to check the function to test.

```python
def addition(x, y):
    return x + y
```

- go to [test_file.py](test_file.py) for the test cases.

```python
from addition import addition

def test_addition_int():
    assert addition(4, 5) == 9
    assert addition(12, 2) == 14

def test_addition_str():
    assert addition('a', 'b') == 'ab'
```

- to test it out, run

```bash
docker build -t pytest-assertion assertion/ && docker run pytest-assertion
```

## Result

```text
============================= test session starts ==============================
platform linux -- Python 3.9.19, pytest-8.2.0, pluggy-1.5.0
rootdir: /test
collected 2 items

test_file.py ..                                                          [100%]

============================== 2 passed in 0.01s ===============================
```
