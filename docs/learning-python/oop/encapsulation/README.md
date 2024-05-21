# Encapsulation

Encapsulation is a fundamental programming technique used to achieve data hiding in OOP.

!!! info

    Encapsulation in OOP refers to binding data and the methods to manipulate that data together in a single unit, that is, class.

Depending upon this unit, objects are created. Encapsulation is usually done to hide the state and representation of an object from outside.
A class can be thought of as a capsule having methods and properties inside it.

## Get and Set

In order to allow controlled access to properties from outside the class, getter and setter methods are used.

!!! note

    A getter method allows reading a property’s value.

    A setter method allows modifying a property’s value.

## Challenge

- Follow on **Task: Implement Complete Student Class** and its Solution

=== "Task"

    ```python
    """
        Implement Complete Student Class

        Task
            Implement the following properties as private:
                name
                rollNumber

            Include the following methods to get and set the private properties above:
                getName()
                setName()
                getRollNumber()
                setRollNumber()

            Implement this class according to the rules of encapsulation.

        Input
            Checking all the properties and methods

        Output
            Expecting perfectly defined fields and getter/setters

        Note: Do not use initializers to initialize the properties. Use the set methods to do so. If the setter is not defined properly, the corresponding getter will also generate an error even if the getter is defined properly.
    """

    class Student:
        def setName(self):
            pass

        def getName(self):
            pass

        def setRollNumber(self):
            pass

        def getRollNumber(self):
            pass
    ```

=== "Solution"

    ```python
    class Student:
        __name = None
        __rollNumber = None

        def setName(self, name):
            self.__name = name

        def getName(self):
            return self.__name

        def setRollNumber(self, rollNumber):
            self.__rollNumber = rollNumber

        def getRollNumber(self):
            return self.__rollNumber


    demo1 = Student()
    demo1.setName("Alex")
    print("Name:", demo1.getName())
    demo1.setRollNumber(3789)
    print("Roll Number:", demo1.getRollNumber())
    ```
