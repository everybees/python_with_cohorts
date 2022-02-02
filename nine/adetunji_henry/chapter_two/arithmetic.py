# an application that prompts the user for two integers
# obtains them and print their sum, product, difference and quotient)

number1 = int(input("Enter your first number here: "))
number2 = int(input("Enter your second number here: "))

add = number1 + number2
product = number1 * number2
difference = number1 - number2
quotient = number1 / number2

print('The sum of {} and {} is {}'.format(number1, number2, add))
print('The product of {} and {} is {}'.format(number1, number2, product))
print('The difference of {} and {} is {}'.format(number1, number2, difference))
print('The quotient of {} and {} is {}'.format(number1, number2, quotient))
