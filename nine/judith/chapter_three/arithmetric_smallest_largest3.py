import sys

smallest_number = sys.maxsize
largest_number = 0
total = 0
product = 1
count = 0
for i in range(4):
    user_input = int(input("Enter a number"))
    count += 1
    total += user_input
    product *= user_input
    if user_input < smallest_number:
        smallest_number = user_input
    if user_input > largest_number:
        largest_number = user_input

average = total / count

print(total, '', product, '', average)
print('the smallest number :', smallest_number)
print('the largest number :', largest_number)
