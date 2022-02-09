number = (int(input('Enter a number to check its factorial  ' )))
factorial = 1
if(number == 1 or number == 0):
    factorial = 1
if (number >=2):
    for counter in range(number,0,-1):
        factorial  *= counter
print(f'{number}! = {factorial}')       