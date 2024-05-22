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

!!! info

    The double underscores mean this is a special method that the Python interpreter will treat as a special case.

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

!!! warning

    It is important to define the initializer with complete parameters to avoid any errors. Similar to methods, initializers also have the provision for optional parameters.

## Challenges

- Take a look on **Task: Calculate Student Performance** and its solution

=== "Task 1"

    ```python
    """
        Calculate Student Performance

        Problem statement
            Implement a class - Student - that has four properties and two methods. All these attributes (properties and methods) should be public. This problem can be broken down into three tasks.

        Task 1
            Implement a constructor to initialize the values of four properties: name, phy, chem, and bio.

        Task 2
            Implement a method – totalObtained – in the Student class that calculates total marks of a student.

        Task 3
            Using the totalObtained method, implement another method, percentage, in the Student class that calculates the percentage of students marks.
            Assume that the total marks of each subject are 100. The combined marks of three subjects are 300.
            Formula: percentage = (marks_obtained/total_marks) * 100
    """

    class Student:
        def __init__(self):
            pass # to fill

        def totalObtained(self):
            pass # to fill

        def percentage(self):
            pass # to fill
    ```

=== "Solution"

    ```python
    class Student:
        def __init__(self, name, phy, chem, bio):
            self.name = name
            self.phy = phy
            self.chem = chem
            self.bio = bio

        def totalObtained(self):
            return(self.phy + self.chem + self.bio)

        def percentage(self):
            return((self.totalObtained() / 300) * 100)
    ```

- Let's continue to **Task: Implement Calculator Class** and its solution

=== "Task 2"

    ```python
    """
        Implement Calculator Class

        Write a Python class called Calculator by completing the tasks below:

        Task 1
            Initializer
            Implement an initializer to initialize the values of num1 and num2.

        Properties
            num1
            num2

        Task 2
            Methods
                add() is a method that returns the sum of num1 and num2.
                subtract() is a method that returns the subtraction of num1 from num2.
                multiply() is a method that returns the product of num1 and num2.
                divide() is a method that returns the division of num2 by num1.

        Input
            Pass numbers (integers or floats) in the initializer.

        Output
            addition, subtraction, division, and multiplication

        Sample input
            obj = Calculator(10, 94);
            obj.add()
            obj.subtract()
            obj.multiply()
            obj.divide()

        Sample output
            104
            84
            940
            9.4
    """

    class Calculator:
        def __init__(self):
            pass

        def add(self):
            pass

        def subtract(self):
            pass

        def multiply(self):
            pass

        def divide(self):
            pass
    ```

=== "Solution"

    ```python
    class Calculator:
        def __init__(self, num1, num2):
            self.num1 = num1
            self.num2 = num2

        def add(self):
            return (self.num2 + self.num1)

        def subtract(self):
            return (self.num2 - self.num1)

        def multiply(self):
            return (self.num2 * self.num1)

        def divide(self):
            return (self.num2 / self.num1)


    demo1 = Calculator(10, 94)
    print("Addition:", demo1.add())
    print("Subtraction:", demo1.subtract())
    print("Mutliplication:", demo1.multiply())
    print("Division:", demo1.divide())
    ```
