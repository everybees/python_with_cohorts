
import sys

maximum= -sys.maxsize
average=0
total=0
minimum= sys.maxsize

total_integer=0


   
for number in range (4):
    integer_number=(input("Enter  integers:  "))
    integer_number=int(integer_number)

    if(integer_number > maximum):
        maximum = integer_number

    if(integer_number < minimum):
        minimum = integer_number
        total_integer+=integer_number
        
        

total+=total_integer
print("The total value is: ",total)



average=total/number
print(f"average is: {average:>.2f}")
print("The minimum value is: ",minimum)
print("The maximum value is: ",maximum)


    