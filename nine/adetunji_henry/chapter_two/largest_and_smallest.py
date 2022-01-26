number1 = int(input("Enter your first number here: "))
number2 = int(input("Enter your second number here: "))
number3 = int(input("Enter your third number here: "))
number4 = int(input("Enter your fourth number here: "))
number5 = int(input("Enter your fifth number here: "))

smallest = (number1, number2, number3, number4, number5)
largest = (number1, number2, number3, number4, number5)
print("\n")

if (number1 > number2) and (number1 > number3) and (number1 > number4) and (number1 > number5):
    largest = number1
elif (number2 > number1) and (number2 > number3) and (number2 > number4) and (number2 > number5):
    largest = number2
elif (number3 > number1) and (number3 > number2) and (number3 > number4) and (number3 > number5):
    largest = number3
elif (number4 > number1) and (number4 > number2) and (number4 > number3) and (number4 > number5):
    largest = number4
else:
    largest = number5
print("The largest of the five numbers is: ", largest)

if (number1 < number2) and (number1 < number3) and (number1 < number4) and (number1 < number5):
    smallest = number1
elif (number2 < number1) and (number2 < number3) and (number2 < number4) and (number2 < number5):
    smallest = number2
elif (number3 < number1) and (number3 < number2) and (number3 < number4) and (number3 < number5):
    smallest = number3
elif (number4 < number1) and (number4 < number2) and (number4 < number3) and (number4 < number5):
    smallest = number4
else:
    smallest = number5
    print("The smallest of the five numbers is: ", smallest)
