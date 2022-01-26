
import sys

import sys
first_largest_number=-sys.maxsize
second_largest_number=-sys.maxsize
user_input_counter=0

for number in range(1,11):
    user_input=int (input("Enter ten number"))
    user_input_counter +=1


    if(user_input > first_largest_number):
        first_largest_number = user_input

    if(user_input > second_largest_number and first_largest_number > second_largest_number):
        second_largest_number=user_input
        



print("The value of the firstnumber is the highestnumber",first_largest_number)
 
print(second_largest_number)  
