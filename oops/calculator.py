"""Create methods for the Calculator class that can do the following:

Add two numbers.
Subtract two numbers.
Multiply two numbers.
Divide two numbers.
Examples
calculator = Calculator()

calculator.add(10, 5) ➞ 15

calculator.subtract(10, 5) ➞ 5

calculator.multiply(10, 5) ➞ 50

calculator.divide(10, 5) ➞ 2
Notes
The methods should return the result of the calculation.
Don't worry about needing to handle division by zero errors.
See the Resources tab for some helpful tutorials on Python classes."""


class Calculator:
    def __init__(self,n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return self.n1 + self.n2

    def substract(self):
        return  self.n1 - self.n2

    def multiply(self):
        return self.n1 * self.n2

    def divide(self):
        return self.n1 // self.n2


cal = Calculator(10,5)
print(cal.add())
print(cal.substract())
print(cal.multiply())
print(cal.divide())