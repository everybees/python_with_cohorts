factorial = 1
result = 1
integer = int(input("Enter a number: "))
for number in range(1):
    for numbers in range(integer):
        result *= (integer - numbers)
    factorial *= result
    print("The factorial of", integer, "is", factorial)