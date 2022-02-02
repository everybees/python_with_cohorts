import math


value1=input("Enter a number:  ")
value2=input("Enter a number:  ")

value1=int(value1)
value2=int(value2)

first_Number=int (math.pow(value1,2))
second_number=int (math.pow(value2,2))

print("firstnumber is ",first_Number)
print("secondnumber is ",second_number)

sum_number=first_Number + second_number
print("The sum of the two number is ",sum_number)


difference_of_two_number=first_Number - second_number
print("The difference of the two is ",difference_of_two_number)
