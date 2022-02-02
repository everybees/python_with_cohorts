import sys

smallest_number = sys.maxsize
largest_number = 0

first_number = int(input("Enter a number"))
second_number = int(input('Enter a number'))
third_number = int(input('Enter a number'))
if first_number >= second_number and first_number >= third_number:
    largest_number = first_number
if second_number >= first_number and second_number >= third_number:
    largest_number = second_number
    if third_number >= second_number and third_number >= first_number:
        largest_number = third_number
if first_number < second_number and first_number < third_number:
    smallest_number = first_number
    if second_number < first_number and second_number < third_number:
        smallest_number = second_number
        if third_number < second_number and third_number < first_number:
            smallest_number = third_number

total = first_number + second_number + third_number
product = first_number * second_number * third_number
average = total / 3
print(total, product, average)
print('smallest number', smallest_number)
print('largest number'), largest_number
