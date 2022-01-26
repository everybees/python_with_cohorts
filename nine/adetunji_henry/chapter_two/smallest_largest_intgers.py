number1 = int(input("Enter your first number here: "))
number2 = int(input("Enter your second number here: "))
number3 = int(input("Enter your third number here: "))
# print("\n")

add = number1 + number2 + number3
average = (number1 + number2 + number3) / 3
product = number1 * number2 * number3
smallest = (number1, number2, number3)
largest = (number1, number2, number3)
print("\n")

print('The sum of {}, {} and {} is {}'.format(number1, number2, number3, add))
print('The average of {}, {} and {} is {}'.format(number1, number2, number3, average))
print('The product of {}, {} and {} is {}'.format(number1, number2, number3, product))

if (number1 > number2) and (number1 > number3):
    largest = number1
elif (number2 > number1) and (number2 > number3):
    largest = number2
else:
    largest = number3
print("The largest number of the three is: ", largest)

if (number1 < number2) and (number1 < number3):
    smallest = number1
elif (number2 < number1) and (number2 < number3):
    smallest = number2
else:
    smallest = number3
    print("The smallest number of the three is: ", smallest)
