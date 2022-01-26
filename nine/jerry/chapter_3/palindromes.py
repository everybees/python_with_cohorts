# 3.12 (Palindromes) A palindrome is a number, word or text phrase that reads the same
# backwards or forwards. For example, each of the following five-digit integers is a palindrome:
# 12321, 55555, 45554 and 11611. Write a script that reads in a five-digit integer
# and determines whether it’s a palindrome. [Hint: Use the // and % operators to separate
# the number into its digits.]
import math

number = int(input("Enter a five-digit number: "))
for numbers in range(1):
    if (number % math.pow(10, 6 - 1)) // math.pow(10, 5 - 1) == (number % math.pow(10, 6 - 5)) // math.pow(10, 5 - 5) \
            and (number % math.pow(10, 6 - 2)) // math.pow(10, 5 - 2) == (number % math.pow(10, 6 - 4)) // math.pow(10, 5 - 4):
        print("This number, ", number, "is a palindrome")
    else:
        print("This number", number, "is not a palindrome")

