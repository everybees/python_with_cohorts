def factorial(number):
    factorial = 1
    for i in range(number, 0, -1):
        factorial *= i
    return factorial
print(factorial(5))
