# (Separating the Digits in an Integer) In Exercise 2.11, you wrote a script that separated
# a five-digit integer into its individual digits and displayed them. Reimplement your
# script to use a loop that in each iteration “picks off” one digit (left to right) using the //
# and % operators, then displays that digit.

number = int(input("Enter a five digit number"))
for i in range(1):
    a = number//10000
    b = (number % 10000)//1000
    c = (number % 1000)//100
    d = (number % 100)//10
    e = number % 10

    new_number = a, b, c, d, e
    print(a, b, c, d, e)


