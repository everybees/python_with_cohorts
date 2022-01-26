# An application that prompts the user for two integers,
# displays if the number entered is the largest or they are both equal

first_number = int(input("Kindly enter your first number here: "))
second_number = int(input("Enter your second number here: "))

if (first_number > second_number):
    print("{} is larger than {}".format(first_number, second_number))
elif (first_number < second_number):
    print("{} is larger than {}".format(second_number, first_number))
else:
    print("These numbers are equal")
