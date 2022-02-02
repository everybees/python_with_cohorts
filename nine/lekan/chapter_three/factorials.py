user_input = int(input('Enter A Number: '))
temp = user_input
product = 1

for i in range(temp):
    product *= temp
    temp -= 1

print('The factorial of ', user_input, ' is ', product)

