# (Nested Control Statements) Use a loop to find the two largest values of 10 numbers
# entered.

from tkinter import N


maximum = 0
second_largest = 0
for number in range(10):
    numbers = int(input("Enter a number "))
    if(numbers > maximum):
        second_largest = maximum
        maximum = numbers
    elif(numbers > second_largest):
        second_largest = numbers

print("Largest Number is :",maximum,"Second Largest Number is:",second_largest)

