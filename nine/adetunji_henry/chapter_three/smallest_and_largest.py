number1 = int(input("Enter your first number here: "))
number2 = int(input("Enter your second number here: "))
number3 = int(input("Enter your third number here: "))
number4 = int(input("Enter your third number here: "))


add = number1 + number2 + number3 + number4
average = (number1 + number2 + number3 + number4) / 4
product = number1 * number2 * number3 * number4
smallest = (number1, number2, number3, number4)
largest = (number1, number2, number3, number4)

print("\n")

print('The sum of {}, {}, {} and {} is {}'.format(number1, number2, number3, number4, add))
print('The average of {}, {}, {} and {} is {}'.format(number1, number2, number3, number4, average))
print('The product of {}, {}, {} and {} is {}'.format(number1, number2, number3, number4, product))

print("\n")

for i in range(3):
    if (number1 > number2) and (number1 > number3) and (number1 > number4):
        largest = number1
    elif (number2 > number1) and (number2 > number3) and (number2 > number4):
        largest = number2
    elif (number3 > number1) and (number3 > number2) and (number3 > number4):
        largest = number3
    else:
        largest = number4
print("The largest of the four numbers is: ", largest)

if (number1 < number2) and (number1 < number3) and (number1 < number4):
            smallest = number1
elif (number2 < number1) and (number2 < number3) and (number2 < number4):
            smallest = number2
elif (number3 < number1) and (number3 < number2) and (number3 < number4):
            smallest = number3
else:
            smallest = number4
print("The smallest of the four numbers is: ", smallest)
