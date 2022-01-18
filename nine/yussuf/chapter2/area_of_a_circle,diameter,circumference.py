import math

def find_diameter_of_a_circle(radius):
    diameter = 2 * radius
    return diameter

def find_circumference_of_a_circle(radius):
    circumference = 2 * math.pi * radius
    return circumference

def find_area_of_a_circle(radius):
    area = math.pi * radius * radius
    return area
    
    
radius = float(input("Enter radius of the circle "))

print("The diameter is ",find_diameter_of_a_circle(radius))
print("The circumference is ",find_circumference_of_a_circle(radius))
print("The area is ",find_area_of_a_circle(radius))