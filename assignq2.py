""" 2. Write a recursive function to calculate the power of a number.
# Objective: To implement the concept of recursive functions in python"""
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent-1)
print(power(2,4))