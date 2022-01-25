factorial = 1
number = int(input('Enter the number to check its factorial:'))
if number == 0:
    print(1)
if number == 1:
    print(1)
# if number >= 2:
while number >= 2:
    factorial *= number
    number -= 1
print('The factorial:', factorial)