""" Solution 2: Implement Calculator Class """

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
