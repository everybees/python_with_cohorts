first_number = float(input('Enter a number'))
second_number = float(input('Enter a number'))
third_number = float(input('Enter a number'))

largest_number = first_number
smallest_number = first_number

if second_number > first_number and second_number > third_number:
    largest_number = second_number
    if third_number > first_number and third_number > second_number:
        largest_number = third_number

print(smallest_number,largest_number)
