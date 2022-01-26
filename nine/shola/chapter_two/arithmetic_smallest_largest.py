# (Arithmetic, Smallest and Largest) Write a script that inputs three integers from
# the user. Display the sum_total, average, product, smallest and largest of the numbers. Note that
# each of these is a reduction in functional-style programming.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
addition = num1 + num2 + num3
average = float(num1 + num2 + num3)/3
product = num1 * num2 * num3

print("The addition of the 3 numbers are: ", int(addition))
print("the average is: ", float(average))
print("the product is: ", int(product))
print("the maximum is: ", max(num1, num2, num3))
print("the minimum is: ", min(num1, num2, num3))
