# (Circle Area, Diameter and Circumference) For a circle of radius 2, display the diameter,
# circumference and area. Use the value 3.14159 for π. Use the following formulas
# (r is the radius): diameter = 2r, circumference = 2πr and area = πr2. [In a later chapter, we’ll
# introduce Python’s math module which contains a higher-precision representation of π.]

# ANSWER

pi = 3.14159
radius_of_circle = 2
diameter_of_circle = 2 * radius_of_circle
circumference_of_circle = 2 * pi * radius_of_circle
area_of_circle = pi * radius_of_circle**2

print('Diameter of the circle is',diameter_of_circle,
'\nCircumference of the circle is',circumference_of_circle,
'\nArea of the circle is', area_of_circle)