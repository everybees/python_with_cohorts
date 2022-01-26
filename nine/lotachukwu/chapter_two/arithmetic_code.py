num1 = int(input('enter a number: '))
num2 = int(input('enter another number: '))
num3 = int(input('enter another number: '))

sums = num1 + num2 + num3
print('Sum is', sums)
average = (num1 + num2 + num3) / 3
print('Average is', average)
multiplication = num1 * num2 * num3
print('The product is', multiplication)

smallest_num = num1
if num2 < smallest_num and num2 < num3:
    smallest_num = num2

if num3 < smallest_num and num3 < num2:
    smallest_num = num3

largest_num = num1
if num2 > largest_num and num2 > num3:
    largest_num = num2
if num3 > largest_num and num3 > num2:
    largest_num = num3
print('largest number is', largest_num)
print('smallest number is', smallest_num)
