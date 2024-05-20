# Class

In Python, classes are defined as follows:

```python
class ClassName:
    pass
```

The `class` keyword tells the compiler that we are creating a custom class, which is followed by the class name and the `:` sign.

All the properties and methods of the class will be defined within the class scope.

## What is an initializer?

As the name suggests, the initializer is used to initialize an object of a class. It’s a special method that outlines the steps that are performed when an object of a class is created in the program. It’s used to define and assign values to instance variables.

The initialization method is similar to other methods but has a pre-defined name, `__init__`.

> The double underscores mean this is a special method that the Python interpreter will treat as a special case.

The initializer is a special method because it does not have a return type. The first parameter of `__init__` is `self`, which is a way to refer to the object being initialized.

It is always a good practice to define it as the first member method in the class definition.

### Defining initializers

Initializers are called when an object of a class is created. See the example below:

```python
class Employee:
    # defining the properties and assigning them None
    def __init__(self, ID, salary, department):
        self.ID = ID
        self.salary = salary
        self.department = department


# creating an object of the Employee class with default parameters
Steve = Employee(3789, 2500, "Human Resources")

# Printing properties of Steve
print("ID :", Steve.ID)
print("Salary :", Steve.salary)
print("Department :", Steve.department)
```

The initializer is automatically called when an object of the class is created. Now that we will be using initializers to make objects, a good practice would be to initialize all of the object properties when defining the initializer.

> It is important to define the initializer with complete parameters to avoid any errors. Similar to methods, initializers also have the provision for optional parameters.

## Challenges

- Follow on [Task 1: Calculate Student Performance](task_1.py) for the problem statement and [Solution 1](solution_1.py) for the solution
- Follow on [Task 2: Implement Calculator Class](task_2.py) for the problem statement and [Solution 2](solution_2.py) for the solution
