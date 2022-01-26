import sys
largest_num = -sys.maxsize
smallest_num = sys.maxsize
sums = 0
average = 0
product = 1
for i in range(4):
    number = int(input("Enter number: "))
    sums += number 
    product *= number
    if number > largest_num:
        largest_num = number 
    if number < smallest_num:
        smallest_num = number
average = sums/4
print(f'largest number is {largest_num} and smalest number is {smallest_num}')
print('Sum is',sums)
print('Average of the numbers is', average)
print('Product of the numbers is', product)