import sys
first_largest_number = -sys.maxsize
second_largest_number = -sys.maxsize

for i in range(10):
    user_input = int (input("Enter an integer: "))
    if user_input > first_largest_number:
        second_largest_number  = first_largest_number
        first_largest_number = user_input

    elif user_input > second_largest_number:
        second_largest_number = user_input

print(f'The largest number in the series is {first_largest_number}')
print(f'The second largest number in the series is {second_largest_number}')