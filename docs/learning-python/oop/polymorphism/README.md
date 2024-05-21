# Polymorphism

Assume there is a parent class named `Shape` from which the child classes `Rectangle`, `Circle`, `Polygon`, and `Diamond` are derived.

Suppose your application will need methods to calculate the area of each specific shape. The area for each shape is calculated differently, which is why you can’t have a single implementation. You could throw in separate methods in each class (for instance, `getSquareArea()`, `getCircleArea()` etc.). But this makes it harder to remember each method’s name.

## Make things simpler with polymorphism

It would be better if all specific area calculation methods could be called getArea(). You would only have to remember one method name and when you call that method, the method specific to that object would be called. This can be achieved in object-oriented programming using polymorphism. The base class declares a function without providing an implementation. Each derived class inherits the function declaration and can provide its own implementation

Consider that the Shape class has a method called `getArea()`, which is inherited by all subclasses mentioned. With polymorphism, each subclass may have its own way of implementing the method. For example, when the `getArea()` method is called on an object of the `Rectangle` class, the method will respond by displaying the area of the rectangle. On the other hand, when the same method is called on an object of the `Circle` class, the circle’s area will be calculated and displayed on the screen.

## Polymorphism through `method`

Consider two shapes that are defined as classes: **Rectangle** and **Circle**. These classes contain the `getArea()` method that calculates the area for the respective shape depending on the values of their properties.

```python
class Rectangle():

    # initializer
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    # method to calculate Area
    def getArea(self):
        return (self.width * self.height)


class Circle():
    # initializer
    def __init__(self, radius=0):
        self.radius = radius
        self.sides = 0

    # method to calculate Area
    def getArea(self):
        return (self.radius * self.radius * 3.142)


shapes = [Rectangle(6, 10), Circle(7)]
print("Sides of a rectangle are", str(shapes[0].sides))
print("Area of rectangle is:", str(shapes[0].getArea()))

print("Sides of a circle are", str(shapes[1].sides))
print("Area of circle is:", str(shapes[1].getArea()))
```

## Polymorphism through Inheritance

Consider the example of a `Shape` class, which is the base class while many shapes like `Rectangle` and `Circle` extending from the base class are derived classes. These derived classes inherit the `getArea()` method and provide a shape-specific implementation, which calculates its area.

```python
class Shape:
    def __init__(self):  # initializing sides of all shapes to 0
        self.sides = 0

    def getArea(self):
        pass


class Rectangle(Shape):  # derived from Shape class
    # initializer
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    # method to calculate Area
    def getArea(self):
        return (self.width * self.height)


class Circle(Shape):  # derived from Shape class
    # initializer
    def __init__(self, radius=0):
        self.radius = radius

    # method to calculate Area
    def getArea(self):
        return (self.radius * self.radius * 3.142)


shapes = [Rectangle(6, 10), Circle(7)]
print("Area of rectangle is:", str(shapes[0].getArea()))
print("Area of circle is:", str(shapes[1].getArea()))
```

## Challenges

- Follow on **Task: Implement Animal Class** and its solution

=== "Task"

    ```python
    """
        Implement Animal Class

        A parent class named Animal.

        Inside it, define:
            name
            sound
            __init__()
            Animal_details() function
                It prints the name and sound of the Animal.

        Then there are two derived classes

        Dog class
            Has a property family
            Has an initializer that calls the parent class initializer in it through super()
            Has an overridden method named Animal_details() which prints detail of the dog.

        Sheep class
            Has a property color
            Has an initializer that calls the parent class initializer in it through super()
            Has an overridden method named Animal_details(), which prints detail of the sheep

        The derived classes should override the Animal_details() method defined in the Animal class.
            The overridden method in Dog class should print the value of family as well as the name and sound.
            The overridden method in Sheep class should print the value of color as well as the name and sound

        Input
            name of Dog is set to Pongo, sound is set to Woof Woof, and family is set to Carnivore in the initializer of Dog object.
            name of Sheep is set to Billy, sound is set to Baaa Baaa, and color is set to White in the initializer of Sheep object.
            Now, call Animal_details() from their respective objects.

        Sample Input
            d = Dog("Pongo", "Woof Woof", "Husky")
            d.Animal_details()
            print(" ")
            s = Sheep("Billy", "Baaa Baaa", "White")
            s.Animal_details()

        Sample Output
            Name: Pongo
            Sound: Woof Woof
            Family: Husky

            Name: Billy
            Sound: Baa Baa
            Color: White
    """

    class Animal:
        pass
        # write your class here

    class Dog(Animal):
        pass
        # write your class here

    class Sheep(Animal):
        pass
    # write your class here
    ```

=== "Solution"

    ```python
    class Animal:
        def __init__(self, name, sound):
            self.name = name
            self.sound = sound

        def Animal_details(self):
            print("Name:", self.name)
            print("Sound:", self.sound)


    class Dog(Animal):
        def __init__(self, name, sound, family):
            super().__init__(name, sound)
            self.family = family

        def Animal_details(self):
            super().Animal_details()
            print("Family:", self.family)


    class Sheep(Animal):
        def __init__(self, name, sound, color):
            super().__init__(name, sound)
            self.color = color

        def Animal_details(self):
            super().Animal_details()
            print("Color:", self.color)


    d = Dog("Pongo", "Woof Woof", "Husky")
    d.Animal_details()
    print("")
    s = Sheep("Billy", "Baa Baa", "White")
    s.Animal_details()
    ```
