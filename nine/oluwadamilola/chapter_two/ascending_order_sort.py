first_number = float((input("Enter the first floating number: ")))
second_number = float((input("Enter the second floating number: ")))
third_number = float((input("Enter the third floating number: ")))

if first_number > second_number and first_number > third_number:
    if second_number > third_number:
        print("The arragement in ascending order is: ", third_number, second_number, first_number)

if first_number > second_number and first_number > third_number:
    if third_number > second_number:
        print("The arragement in ascending order is: ", second_number, third_number, first_number)


if second_number > first_number and second_number > third_number:
    if first_number > third_number:
        print("The arragement in ascending order is: ", third_number,first_number,second_number)

if second_number > first_number and second_number > third_number:
    if third_number > first_number:
        print("The arragement in ascending order is: ", first_number,third_number,second_number)

if third_number > first_number and third_number > second_number:
    if first_number > second_number:
        print("The arragement in ascending order is: ", second_number, first_number, third_number) 

if third_number > first_number and third_number > second_number:
    if second_number > first_number:
        print("The arragement in ascending order is: ", first_number, second_number, third_number) 