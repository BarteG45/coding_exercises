#DESCRIPTION
'''Write a function calculate_hypotenuse(a, b) that takes the lengths of the two shorter sides of a right triangle and returns the length of the hypotenuse using the Pythagorean theorem.'''

#MY SOLUTIONS 
import math
def calculate_hypotenuse(a,b):
    c = math.sqrt(a**2 + b**2)
    return (f"The length of the hypotenuse is: {c}")


def calculate_hypotenuse(a,b):
    c = (a**2 + b**2)**0.5
    return (f"The length of the hypotenuse is: {c}")