from math import factorial



total_number=0


for user_input in range (1):
    user_input=input("Enter a number")
    user_input=int(user_input)

    if(total_number+user_input==total_number):
        print(total_number)