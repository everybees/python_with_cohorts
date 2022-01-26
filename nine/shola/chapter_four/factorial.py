factorial = 1
number = int(input("Enter a Number"))
if number == 0 and number == 1:
    print(factorial)
else:
    while number >= 2:
        factorial *= number
        number = number - 1
print(factorial)





