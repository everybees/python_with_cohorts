# 3.13 (Factorials) Factorial calculations are common in probability. The factorial of a
# non-negative integer n is written n! (pronounced “n factorial”) and is defined as follows:
# n! = n · (n - 1) · (n - 2) · … · 1
# for values of n greater than or equal to 1, with 0! defined to be 1. So,
# 5! = 5 · 4 · 3 · 2 · 1
# which is 120. Factorials increase in size very rapidly.
# Write a script that inputs a non-negative integer and computes and displays its factorial.
# Try your script on the integers 10, 20,
# 30 and even larger values. Did you find any integer input for which Python could not
# produce an integer factorial value?


factorial = 1
result = 1
integer = int(input("Enter a number: "))
for number in range(1):
    for numbers in range(integer):
        result *= (integer - numbers)
    factorial *= result
    print("The factorial of", integer, "is", factorial)