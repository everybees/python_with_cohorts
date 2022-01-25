def factorial(number):
    factorials = 1
    for i in range(1, number):
        factorials *= i
    return factorials


print(factorial(6))


def addition(number1,number2):
    return number1 + number2


def multiplication(number1, number2):
    return number1 * number2


def reverse(number):
    reverse_number = 0
    while number != 0:
        digit = number % 10

        reverse_number = reverse_number * 10 + digit

        number = number // 10

    return reverse_number


reverse(23)
print(reverse(23))


