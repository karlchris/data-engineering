# Inheritance

## Definition

Inheritance provides a way to create a new class from an existing class.
The new class is a specialized version of the existing class such that it inherits all the non-private fields (variables) and methods of the existing class.
The existing class is used as a starting point or as a base to create the new class.

## The IS A Relationship

After reading the above definition, the next question that comes to mind is this: when do we use inheritance? Wherever we come across an IS A relationship between objects, we can use inheritance.

![inheritance ilustration](../icons/inheritance-ilustration.png)

In the above illustration, we can see the objects have a _IS A_ relationship between them. We can write it as:

- Square _IS A_ shape
- Python _IS A_ programming language
- Car _IS A_ vehicle

## What is the `super()` function?

The use of `super()` comes into play when we implement inheritance. It is used in a child class to refer to the parent class without explicitly naming it. It makes the code more manageable, and there is no need to know the name of the parent class to access its attributes.

> Note: Make sure to add parenthesis at the end to avoid a compilation error.

```python
class Vehicle:  # defining the parent class
    fuelCap = 90


class Car(Vehicle):  # defining the child class
    fuelCap = 50

    def display(self):
        # accessing fuelCap from the Vehicle class using super()
        print("Fuel cap from the Vehicle Class:", super().fuelCap)

        # accessing fuelCap from the Car class using self
        print("Fuel cap from the Car Class:", self.fuelCap)


obj1 = Car()  # creating a car object
obj1.display()  # calling the Car class method display()
```

## Advantages

- Reusability: Inheritance makes the code reusable
- Less code modification, less risky
- Extensibility: Using inheritance, one can extend the base class as per the requirements of the derived class
- Important data hiding: The base class can keep some data private so that the derived class cannot alter it. This concept is called encapsulation.

## Challenges

- Follow on [Task: Handling Bank Account](task.py) for the problem statement and [Solution](solution.py) for the solution
