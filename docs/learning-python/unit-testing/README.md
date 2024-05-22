# Unit Testing

There are several types of software application testing that are commonly used in the software development lifecycle to ensure the quality and reliability of software applications

![testing hierarchy](icons/testing-hierarchy.png)

Unit testing is a critical software testing technique used to validate the behavior and functionality of individual units or components in a software application. Automated testing tools are used to ensure that the units are working as intended and meet the specified requirements.

Unit testing also promotes better code design and modularity by encouraging developers to write modular and loosely coupled code that is easier to test and maintain.
It can also improve code reuse and reduce the overall development time and costs by detecting issues early in the development cycle and reducing the need for manual testing and debugging.

**Refactoring** is the process of improving the design of code without changing its external behavior. Unit tests can help ensure that refactoring does not introduce defects into the application.

As in this example, we will be using one of the famous Python library `pytest`

- [assertion](assertion/README.md)
- [exceptions](exceptions/README.md)
- [fixtures](fixtures/README.md)
- [decorator](decorator/README.md)
- [parametrizing](parametrizing/README.md)
- [mocking](mocking/README.md)

## Pytest configuration

**Pytest configuration** is a powerful tool that allows users to customize the behavior of pytest

### Overview of configuration files

Pytest allows users to specify configuration options using configuration files. Configuration files can be used to set command-line options, define fixtures, and specify other options that control pytest’s behavior. There are two types of configuration files that pytest supports: `pytest.ini` and `conftest.py`.

The `pytest.ini` files are INI-style configuration files that can be placed in the root directory of a project or in any directory that contains tests.

The `conftest.py` files are Python files that can be placed in any directory, and they are used to define fixtures and other objects that can be used in tests.

Reference: [Mastering Unit Testing with Pytest](https://www.educative.io/courses/mastering-unit-testing-with-pytest)
