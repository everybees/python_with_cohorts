import math

radius = float(input("Enter the radius of this circle: "))
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print("The area of this circle is {:.2f}".format(area))
print("The circumference of this circle is {:.2f}".format(circumference))
