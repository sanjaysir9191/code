"""    5. Write a python program to add two distance objects with member variables feet and inches using operator overloading.
Objective: To implement the concept of operator overloading in python"""
class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        return f"{self.feet} feet {self.inches} inches"

    def __add__(self):
        total_feet = self.feet 
        total_inches = self.inches 

    
        extra_feet = total_inches//12
        total_feet += extra_feet
        total_inches %= 12
        return Distance(total_feet, total_inches)
    


    
d1 = Distance(4, 4)
d2 = Distance(3, 8)
print("Distance 1:", d1)
print("Distance 2:", d2)
d3 = d1 + d2
print("Total Distance:", d3)