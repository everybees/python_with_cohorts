num = input('Enter a number: ')
if len(num) == 5:
    # for i in range(len(num)):
    number = int(num)
    first_digit = number // 10000
    print(first_digit, end=" ")
    second_digit = (number % 10000) // 1000
    print(second_digit, end=" ")
    third_digit = (number % 1000) // 100
    print(third_digit, end=" ")
    fourth_digit = (number % 100) // 10
    print(fourth_digit, end=" ")
    fifth_digit = number % 10
    print(fifth_digit)
else:
    print("Invalid length of number")
