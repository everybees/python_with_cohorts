first_integer = int (input("Enter the first integer: "))
second_integer = int (input("Enter the second integer: "))
third_integer = int (input("Enter the third integer: "))

sum = first_integer + second_integer + third_integer
average = sum / 3
product = first_integer * second_integer * third_integer
smallest = min(first_integer, second_integer, third_integer)
largest = max (first_integer, second_integer, third_integer)

print("The sum of the three numbers is : ", sum)
print("The average of the three numbers is : ", average)
print("The product of the three numbers is : ", product)
print("The smallest of the three numbers is : ", smallest)
print("The largest of the three numbers is : ", largest)
