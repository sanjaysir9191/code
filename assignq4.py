""" Write a python program to create a base class Calculator. Inherit subclass from it to calculate addition, difference and multiplication of numbers.
Objective: To implement the concept of inheriatnce in python"""

# Base class Calculator
class Calculator:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

class child(Calculator):
    
    def add(self):
        return self.n1 + self.n2

    def sub(self):
        return (self.n1 - self.n2)

    def multi(self):
        return self.n1 * self.n2

obj=child(8,2)
print(obj.add())
print(obj.sub())
print(obj.multi())
