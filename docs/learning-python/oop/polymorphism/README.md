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

- Follow on [Task: Implement Animal Class](https://github.com/karlchris/data-engineering/blob/master/docs/learning-python/oop/polymorphism/task.py) for the problem statement and [Solution](https://github.com/karlchris/data-engineering/blob/master/docs/learning-python/oop/polymorphism/solution.py) for the solution
