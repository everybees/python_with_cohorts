# 2.10 (Arithmetic, Smallest and Largest) Write a script that inputs three integers from
# the user. Display the sum, average, product, smallest and largest of the numbers. Note that
# each of these is a reduction in functional-style programming.

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))

addition = first_number + second_number + third_number
print("The sum is " + str(addition))

average = addition / 3
print("The average is " + str(average))

if first_number > second_number and first_number > third_number:
    print("The largest number is " + str(first_number))
elif second_number > first_number and second_number > third_number:
    print("The largest number is " + str(second_number))
else:
    print("The largest number is " + str(third_number))

if first_number < second_number and first_number < third_number:
    print("The smallest number is " + str(first_number))
elif second_number < first_number and second_number < third_number:
    print("The smallest number is " + str(second_number))
else:
    print("The smallest number is " + str(third_number))
