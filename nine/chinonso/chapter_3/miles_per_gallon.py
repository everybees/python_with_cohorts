sum_gallon = 0
sum_miles = 0
counter = 0
for i in range(4):
    gallon =int(input('Enter the gallon used:'))
    miles = int(input('Enter the miles:'))
    sum_gallon += gallon
    sum_miles += miles
average = sum_miles/sum_gallon
print('The overall average miles/gallon is 'f'{average:.2f}')


