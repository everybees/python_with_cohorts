
factorial = 1
number = int(input("Enter a number to see the factorial: "))

if number == 0:
    print(factorial)

if number == 1:
    print(factorial)

for i in range(1, number + 1):
    factorial = factorial * i
print("The factorial is", factorial)


