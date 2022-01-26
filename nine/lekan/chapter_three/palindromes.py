user_input = int(input('Enter A Five Digit Number: '))
first_digit = user_input // 10000
second_digit = (user_input % 10000) // 1000
third_digit = (user_input % 1000) // 100
fourth_digit = (user_input % 100) // 10
fifth_digit = (user_input % 10) // 1

if fifth_digit == first_digit and fourth_digit == second_digit:
    print('Its a palindrome!!!!!!')
else:
    print('It is not a palindrome!!!!!!!')
