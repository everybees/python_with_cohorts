user_input = int(input("Enter a five digit number"))

first_digit = user_input // 10000
second_digit = (user_input % 10000) // 1000
third_digit = (user_input % 1000) // 100
fourth_digit = (user_input % 100) // 10
fifth_digit = (user_input % 10) // 1

print(first_digit, second_digit, third_digit, fourth_digit, fifth_digit, sep='   ')


