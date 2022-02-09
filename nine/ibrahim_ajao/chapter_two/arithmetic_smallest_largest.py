import sys

sum_total = 0
average = 0
product = 1
minimum = sys.maxsize
maximum = -sys.maxsize
for i in range(4):
    number = int(input('Enter a number'))
    sum_total = sum_total + number
    average = sum_total/4
    product = product * number
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number
print('Total Sum is: ', sum_total)
print('Average is: ', average)
print('Product is : ', product)
print(minimum, maximum)