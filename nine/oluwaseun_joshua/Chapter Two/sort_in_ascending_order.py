first_number=input("enter a number: ")
second_number=input("enter a number: ")
third_number=input("enter a number: ")


first_number=float(first_number)

second_number=float(second_number)

third_number =float(third_number)


first_highest_number=0.0
second_highest_number= 0.0
lowest_number=0.0


# first_number=float(first_number)

# second_number=float(second_number)

# third_number =float(third_number)

if(first_number > second_number > third_number):
    first_highest_number=first_number
    print("The firstnumber is the highest: ",first_highest_number)

elif(first_number > second_number < third_number):
    second_highest_number=first_number
    print("The  firstnumber is the second highest number: ",second_highest_number)


elif(first_number < second_number < third_number):
    lowest_number=first_number
    print("The firstnumber is the lowest number: ",lowest_number)


if(second_number > first_number > third_number):
    first_highest_number=second_number
    print("The secondnumber is the highest: ",first_highest_number)

elif(second_number > first_number < third_number):
    second_highest_number=second_number
    print("The  secondnumber is the second highest number: ",second_highest_number)


elif(second_number < first_number < third_number):
    lowest_number=second_number
    print("The secondnumber is the lowest number: ",lowest_number)


if(third_number > first_number > second_number):
    first_highest_number=third_number
    print("The thirdnumber is the highest: ",first_highest_number)

elif(third_number > first_number < second_number):
    second_highest_number=third_number
    print("The  thirdnumber is the second highest number: ",second_highest_number)


elif(third_number < first_number < second_number):
    lowest_number=third_number
    print("The thirdnumber is the lowest number: ",lowest_number)


