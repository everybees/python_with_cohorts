# (Separating the Digits in an Integer) In Exercise 2.11, you wrote a script that separated
# a five-digit integer into its individual digits and displayed them. Reimplement your
# script to use a loop that in each iteration “picks off” one digit (left to right) using the //
# and % operators, then displays that digit.

number = (input("Enter a five digit number"))
for i in (number):
    print(i, end=" ")


