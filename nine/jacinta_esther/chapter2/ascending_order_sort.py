import sys

minimum = sys.maxsize
count = 0
count_1 = 0
second_highest_number = 0
while count < 1:
    maximum = float(input("Enter a number in decimal1: "))
    if maximum < minimum: minimum = maximum
    for i in range(2):
        number_input = float(input("Enter a number in decimal: "))
        if number_input > maximum:
            second_highest_number = maximum
            maximum = number_input
        elif number_input > second_highest_number:
            if count == 2: second_highest_number = number_input
    count += 1

print("The number in ascending order is:", minimum, second_highest_number, maximum)
print("The number in descending order is:", maximum, second_highest_number, minimum)
