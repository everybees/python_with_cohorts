number = input("Enter a number to check if it is a leap year: ")
number_1 = int(number)
if (number_1 % 4 == 0 and number_1 % 100 != 0) or (number_1 % 100 == 0 and number_1 % 400 == 0):
    print(number_1, "is a leap year ")
else:
    print(number_1, "is not a leap year")
