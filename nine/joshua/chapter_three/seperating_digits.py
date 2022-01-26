# Author: Joshua
# Title : 3.9
number = int(input("Type an integer"))
num1 = number
for i in (4, 3, 2, 1, 0):
    base_number = 10**i

    first = num1 // base_number
    num1 = num1 % base_number

    print(first, "", end="")
