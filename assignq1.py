"""  1. Write a python program to perform the following
        a.  Implement addition of numbers using functions with all parameter types.
        b. Implement lambda function for calculating the square of a number.
        c. Implement recursive function for calculating factorial of a number.
Objective: To implement the concept of functions in python 
"""

# default argument 
def function1(a=5,b=5):
    c=a+b
    return c
    # print(c)
x=function1()    
x1= function1(50,50) 
x2= function1(50)   
print(x)
print(x1)
print(x2)
# keyword argument
def function2(name="sanjay"):
    return (name +" "+ "gupta")
a=function2(name="abhi")
a1=function2('divyam')
print(a)
print(a1)
# positional argument
def function3(name,age):
    print("name",name)
    print("age is ",age)
function3("sanjay Gupta",24)
# print(b)
# arbitary keyword argument 
def function4(**kwargs):
    print(kwargs)
function4(name="sanjay",age=24)
function4(x=88,y="ramesh",z="hajh")

# (B). Implement lambda function for calculating the square of a number.

square =lambda a:a*a
print(square(7))

#  c. Implement recursive function for calculating factorial of a number.

def factorial(n):
        if n==1:
            return 1
        else:
            return n*factorial(n-1)
print(factorial(7))
        