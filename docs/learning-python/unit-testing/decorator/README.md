## Mark Decorator

**Pytest marking** is a feature that enables categorizing tests and applying specific behaviors or actions to them.
It involves tagging tests with markers, which can then be utilized to select, filter, or customize how the tests are executed.
Pytest provides several built-in markers, such as `@pytest.mark.skip` to skip a test and `@pytest.mark.parametrize` to parametrize a test function with multiple input values

Marks are applied to test functions or classes using the `@pytest.mark.<MARKER_NAME>` decorator.

## Expected failure

This marker marks the test as an expected failure.

```python
import pytest

@pytest.mark.xfail
def test_example():
    assert 1 + 1 == 3
```

## Conditionally skipping the test

This marker skips the test if the condition inside evaluated to `True`.

```python
import sys
import pytest

@pytest.mark.skipif(sys.version_info.major == 3 and sys.version_info.minor < 9,
                    reason="requires Python 3.9 or higher")
def test_something():
    assert True
```

## Skipping the test

This marker skips the test.

```python
import pytest

@pytest.mark.skip(reason="test is not ready yet")
def test_example():
    assert 1 + 1 == 2
```

## Parametrizing the test

We can parametrize a test with multiple sets of input values.

```python
import pytest

@pytest.mark.parametrize("test_input,expected_output", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected_output):
    assert eval(test_input) == expected_output
```

## Mark as a fixture

Using `@pytest.mark.usefixtures` decorator can be beneficial when we want to reuse a fixture across multipple tests or ensure that a fixture is always used in a particular test.

```python
# conftest.py

import pytest

@pytest.fixture
def my_fixture():
    return [1,2,3]

# test_file.py

@pytest.mark.usefixtures("my_fixture")
def test_with_fixtures():
    assert True
```
