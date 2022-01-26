# 2.5 (Circle Area, Diameter and Circumference) For a circle of radius 2, display the diameter, circumference and area.
# Use the value 3.14159 for π. Use the following formulas
# (r is the radius): diameter = 2r, circumference = 2πr and area = πr2. [In a later chapter, we’ll
# introduce Python’s math module which contains a higher-precision representation of π.]

import math

radius = 2
pi = 3.14159
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * math.pow(radius, 2)
print("The diameter is", end=" ")
print(diameter, end=". ")
print("The circumference is", end=" ")
print(circumference, end=". ")
print("The area is", end=" ")
print(area)
