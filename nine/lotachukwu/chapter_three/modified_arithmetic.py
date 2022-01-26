import sys

largest_num = -sys.maxsize
smallest_num = sys.maxsize
sums = 0
average = 0
product = 1

for i in range(4):
    num = int(input('enter a number: '))
    sums += num
    average = sums/4
    product *= num
    if num > largest_num:
        largest_num = num
    if num < smallest_num:
        smallest_num = num
print(f'largest number is {largest_num} and smallest is {smallest_num}')
print('sum of numbers is', sums)
print('average of numbers is', average)
print('product of numbers is', product)

