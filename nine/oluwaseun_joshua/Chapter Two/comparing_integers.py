import math
Highest_number=100

first_number=input("Enter a number: ")
# second_number=input("Enter a number: ")

First_number=int(first_number)
# Second_number=int(second_number)
integer_number =int(math.pow(First_number,2))

if(integer_number > Highest_number):
    print("Number is greater than 100")

if(integer_number < Highest_number):
    print("Number is less than 100")

if(integer_number == Highest_number):
    print("Number is equal to 100")

