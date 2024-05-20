# Fixtures

Fixtures allow us to create reusable code that can be used across multiple tests.
A **fixture** is a function that returns an object that will be used in our tests.
They can be used to set up preconditions or data for a test or to clean up after a test.
Pytest fixtures are used to make testing code easier and more efficient.
They can be used to create test data, set up database connections and more.

Fixtures can provide their values to test functions using `return` or `yield` statements.

## Configuration file

In pytest, `conftest.py` is a special file that allows us to define fixtures, hooks, and plugins that can be shared across multiple test files in a directory or its subdirectories.

Fixtures defined in a `conftest.py` file can be used by any test without importing them. Pytest discovers them automatically.

fixtures are defined using `@pytest.fixture` decorator.

```python
# test_file.py
def test_data(data): # this test will pass
    assert 'key' in data

def test_list(lst): # this test will fail and list fixture will be printed
    assert len(lst) == 5, lst
```

```python
# conftest.py
import pytest

@pytest.fixture
def data():
    return {'key': 'value'}

@pytest.fixture
def lst():
    return [1, 2, 3, 4]
```

## Scope parameter

Fixtures can be customized with the help of the `scope` parameter that determines when the fixture is called and when it is destroyed. The `scope` parameter in fixtures defines the lifetime of the fixture.

- `function`: default scope for a fixture, called once test function is invoked and destroyed after it finished.
- `class`: called once each test class that uses it and destroyed if it finished all the test methods in the class.
- `module`
- `session`: called in entire test session and destroyed after test session is completed.
