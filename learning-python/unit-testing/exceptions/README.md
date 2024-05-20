# Testing Exceptions

We will delve into testing for exceptions in Python using pytest. As developers, we strive to write resilient code that can handle all possible scenarios.
A robust code should be designed to handle exceptions effectively. Exceptions are unexpected events or errors that might occur during the execution of a program, and they can disrupt the normal flow of code execution.
By properly handling exceptions, we can prevent crashes and unexpected behaviors and ensure that the code continues to operate gracefully.

Let's take a step back and understand what context managers and exceptions in Python are.

## Context managers

**Context managers** in Python are a way to manage resources like files, network connections, and databases in an efficient manner (pythonic way).
They ensure that resources are properly acquired and releases, no matter what.
The `with` statement in Python is commonly used with context managers.
It allows us to define a block of code that uses a resource and automatically handles the release of resource.

```python
# Opening a file using context manager
with open("file.txt", "r") as file:
    data = file.read()
    print(data)
```

## Exceptions

**Exceptions** in Python are events that occur during the execution of program and disrupt the normal flow of code execution.
They are raised when an error or exceptional conditions occur in the program, such as invalid operation, unexpected input, or a runtime error.
Exceptions are Python's way of handling errors and providing a mechanism to handle them gracefully. It's very important aspect of writing robust and reliable Python code.
Exceptions in Python can be raised explicitly using the `raise` statement or automatically raised by the Python interpreter when it encounters an error condition.

```python
def divide_number(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    else:
        return result

print(divide_numbers(10, 2)) # Output: 5.0
print(divide_numbers(10, 0)) # Output: Error: Division by zero is not allowed!
```

Python provides a variety of built-in exceptions that cover a wide range of error conditions, such as: `TypeError`, `ValueError`, `FileNotFoundError`, etc

## Pytest - Exception Testing

- check the [division.py](division.py)

```python
def divide_numbers(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
```

- check the [test_file.py](test_file.py)

```python
import pytest

from division import divide_numbers

def test_divide_numbers():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)
```

- to test it out, run

```bash
docker build -t pytest-exceptions exceptions/ && docker run pytest-exceptions
```

## Result

```text
============================= test session starts ==============================
platform linux -- Python 3.9.19, pytest-8.2.0, pluggy-1.5.0
rootdir: /test
collected 1 item

test_file.py .                                                           [100%]

============================== 1 passed in 0.01s ===============================
```
