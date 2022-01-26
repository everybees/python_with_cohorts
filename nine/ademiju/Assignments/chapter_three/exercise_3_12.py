# (Palindromes) A palindrome is a number, word or text phrase that reads the same
# backwards or forwards. For example, each of the following five-digit integers is a palindrome:
# 12321, 55555, 45554 and 11611. Write a script that reads in a five-digit integer
# and determines whether it’s a palindrome. [Hint: Use the // and % operators to separate
# the number into its digits.]


number = int(input("Enter a five digit number: "))
first_digit = number // 10000
remainder = number % 10000
second_digit = remainder // 1000
remainder1 = remainder % 1000
third_digit = remainder1 // 100
remainder2 = remainder1 % 100
fourth_digit = remainder2 // 10
fifth_digit = remainder2 % 10
if(first_digit == fifth_digit):
    if(second_digit == fourth_digit):
        print(number,"is a PALINDROME")
    else:
        print(number,"is NOT a Palindrome")
else:
    print(number,"is NOT a Palindrome")