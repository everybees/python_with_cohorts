integer_numbers = int(input("Enter five digits number"))
first_digit = integer_numbers // 10000
second_digit = (integer_numbers % 10000)//1000
third_digit = (integer_numbers % 1000)//100
fourth_digit = (integer_numbers % 100)//10
fifth_digit = (integer_numbers % 10)

print(first_digit, second_digit, third_digit, fourth_digit, fifth_digit)

