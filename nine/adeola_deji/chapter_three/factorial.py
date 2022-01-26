number = int(input("Enter a number to find the factorial: "))
total = 1

for i in range(number, 0, -1):
    total *= i
print(total)