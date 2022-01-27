import sys
sum = 0
average = 0
product = 1
minimum_number = sys.maxsize
maximum_number = -sys.maxsize

for user_input in range(4):
    user_input = int(input('Enter an integer: '))
    sum+= user_input
    product *= user_input
    if user_input > maximum_number:
        maximum_number = user_input
    if user_input < minimum_number:
        minimum_number = user_input       

average = sum / 4
print('The total of the integers is ', sum)
print('The product of the integers is ', product)
print(f'The average of the integers is: {average}')
print('The largest of the integersis: ', maximum_number)
print('THe smallest of the integers is: ', minimum_number)
