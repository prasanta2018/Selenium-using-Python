'''
Circle Program
'''
from math import  pi
class circle:
    def circle_area(self,radius):
        if type(radius) not in [int, float]:
            raise TypeError("The radius must be a non-negative real number")
       
        if radius < 0:
            raise ValueError("The radius cannot be negative.")
        return pi * (radius ** 2)