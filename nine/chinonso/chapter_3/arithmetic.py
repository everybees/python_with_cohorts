import sys
counter = 0
sum = 0
product = 1
maxi = -sys.maxsize
mini = sys.maxsize
for i in range(4):
    number = int(input('Enter the integer:'))
    sum += number
    product *= number
    if number > maxi:
        maxi = number
    if number< mini:
        mini = number

average = float(sum /i)
print('Sum :',sum)
print('Product:',product)
print('Average:',f'{average:.3f}')
print('Smallest:',mini)
print('largest:',maxi)
