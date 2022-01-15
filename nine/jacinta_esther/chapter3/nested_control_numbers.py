count = 0
count_1 = 0
second_highest_number = 0
while count < 1:
    maximum = int(input("Enter a number: "))
    for i in range(9):
        number_input = int(input("Enter a number: "))
        if number_input > maximum:
            second_highest_number = maximum
            maximum = number_input
        elif number_input > second_highest_number:
            if count == 2: second_highest_number = number_input
    count += 1

print("The largest number is:",  maximum)
print("The second largest number is:", second_highest_number)