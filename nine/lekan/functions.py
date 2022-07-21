def factorial(number):
    factorials = 1
    for i in range(1, number):
        factorials *= i
    return factorials


print(factorial(6))


def addition(number1, number2):
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


def free_flow(a_string=str, an_int=0, a_float=0.0, a_list=None, a_dict={}):
    if a_list is None:
        a_list = []
    print(a_string)
    print(type(a_string))
