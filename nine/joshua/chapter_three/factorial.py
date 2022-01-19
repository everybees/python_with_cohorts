# Author: Joshua
# Title : Factorials 3.13

factorial = 1
number = int(input("please enter a digit: "))
if number == 0 or number == 1:
    print(1)
else:
    while number >= 1:
        factorial *= number
        number = number -1

print(factorial)
