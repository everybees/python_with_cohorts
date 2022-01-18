number = int(input('Enter a number'))
print(number)
factorial_int = 1
if number > 0:
    for i in range(number):
        factorial_int *= number
        number -= 1
print('The factorial is ', factorial_int)
