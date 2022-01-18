print('Enter two integers, and I will tell you',
      'the relationships they satisfy.')

number1 = int(input('Enter first integer: '))

number2 = int(input('Enter second integer: '))

numbers_are_equal = number1 == number2
if numbers_are_equal:
    print(number1, ' is equal to ', number2)
else:
    print(number1, ' is not equals to ', number2)

number_one_is_lesser_than_number_two = number1 < number2
if number_one_is_lesser_than_number_two:
    print(number1, ' is less than ', number2)
elif number1 > number2:
    print(number1, ' is greater than ', number2)

number_one_is_lesser_than_or_equal_to_number_two = number1 <= number2
if number_one_is_lesser_than_or_equal_to_number_two:
    print(number1, ' is less than or equals to ', number2)
else:
    print(number1, ' is greater than or equals to ', number2)
