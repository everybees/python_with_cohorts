# (Factorials) Factorial calculations are common in probability. The factorial of a
# nonnegative integer n is written n! (pronounced “n factorial”) and is defined as follows:
# n! = n · (n - 1) · (n - 2) · … · 1
# for values of n greater than or equal to 1, with 0! defined to be 1. So,
# 5! = 5 · 4 · 3 · 2 · 1
# which is 120. Factorials increase in size very rapidly. Write a script that inputs a nonnegative
# integer and computes and displays its factorial. Try your script on the integers 10, 20, 30 and even
# larger values. Did you find any integer input for which Python could not produce an integer factorial value?

number = (int(input('Enter a number to check its factorial  ' )))
factorial = 1
if(number == 1 or number == 0):
    factorial = 1
if (number >=2):
    for counter in range(number,0,-1):
        factorial  *= counter
print(f'{number}! = {factorial}')      


# After trying larger value Python could sill produce their integer factorial only that it took several
#  minutes before computing the results
name = "Ade"
num = name * 5
print(num)