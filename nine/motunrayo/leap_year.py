number = input("Enter a number")
number_one = int(number)
if(number_one % 4 == 0 and number_one % 100 != 0) or (number_one % 100 == 0 and number_one % 400 == 0):
 print("It is a leap year")
else:
 print("It's not a leap year")