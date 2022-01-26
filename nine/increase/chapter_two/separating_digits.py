# (Separating the Digits in an Integer) Write a script that inputs a five-
# digit integer from the user. Separate the number into its individual digits.
# Print them separated by three spaces each. For example, if the user types
# in the number 42339, the script should print
# 4 2 3 3 9
# Assume that the user enters the correct number of digits. Use both the
# floor division and remainder operations to “pick off” each digit.



user_input = int(input('Enter a five digit integer: '))

first_digit = user_input // 10000
first_digit_remainder = user_input % 10000
second_digit = first_digit_remainder // 1000
second_digit_remainder = first_digit_remainder % 1000
third_digit = second_digit_remainder // 100
third_digit_remainder = second_digit_remainder % 100
fourth_digit = third_digit_remainder // 10
fifth_digit =third_digit_remainder % 10


print(first_digit,'\t', second_digit,'\t', third_digit, '\t', fourth_digit, '\t', fifth_digit )