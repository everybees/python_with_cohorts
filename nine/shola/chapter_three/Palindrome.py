# 3.12 (Palindromes) A palindrome is a number, word or text phrase that reads the same
# backwards or forwards. For example, each of the following five-digit integers is a palindrome:
# 12321, 55555, 45554 and 11611. Write a script that reads in a five-digit integer
# and determines whether it’s a palindrome. [Hint: Use the // and % operators to separate
# the number into its digits.]

number = int(input('Enter a five digit number'))
# for i in range (1, 6):
a = number // 10000
b = (number % 10000) // 1000
c = (number % 1000) // 100
d = (number % 100) // 10
e = number % 10
if a == e and b == d:
    print('number is a Palindrome')
else:
    print('number is not a Palindrome')
