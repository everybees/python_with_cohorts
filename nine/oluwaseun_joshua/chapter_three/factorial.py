from math import factorial


total_number=1
number=0

user_input=int(input("Enter a number: "))
# user_input=int(user_input)
for i in range(user_input, 1, -1):
    
    if(user_input==0):
       print(1)

    if(user_input==1):
        print(1)

    if(user_input > 1):
        total_number *=user_input
        user_input -=1

    
     
print(total_number)

