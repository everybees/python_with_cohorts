user_input = int(input('''Enter A Number in 0's and 1's '''))

num = user_input
decimal_value = 0
base = 1

temp = num

temp_is_not_zero = temp > 0
while temp_is_not_zero:
    last_digit = temp % 10
    temp = temp // 10
    decimal_value += last_digit * base
    base = base * 2

print('The decimal equivalent of ', user_input, 'is ', decimal_value)
