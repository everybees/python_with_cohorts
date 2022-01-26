number = int(input("Enter a number to find factorial-> "))

factorial = 1

if number == 0:
    print(1)
elif number == 1:
    print(1)
else:
    while number >= 2:
        factorial *= number
        number = number -1
print(factorial)
