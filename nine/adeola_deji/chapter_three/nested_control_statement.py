import sys


value = 0
count = 0
largest_number = -sys.maxsize
second_largest = -sys.maxsize

while count < 3:
    value = int(input("Enter numbers: "))
    if value > largest_number:
        second_largest = largest_number
        largest_number = value
    elif value > second_largest:
        largest_number = value
    count += 1

print(largest_number, second_largest)