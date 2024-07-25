"""    3. Create a class Room with length, breadth and height as member variable and area as member method. Create different object of Room class and display the area.
Objective: To implement the concept of classes and objects in python
"""
class Room:
    def __init__(self,length,breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height

    def area(self):
        return self.length * self.breadth
    
r1 = Room(5, 6, 3)
r2 = Room(10, 12, 8)
print("Area of Room1: ", r1.area())  
print("Area of Room2: ", r2.area()) 