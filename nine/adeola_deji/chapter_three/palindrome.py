number = int(input("Enter a number: "))
string_num = str(number)

first_digit = number/10000
second_digit = (number % 10000)/ 1000
third_digit = (number % 1000)/100
fourth_digit = (number % 100)/10
fifth_digit = (number % 10) / 1

for i in range(len(string_num, 0)):
    for j in range(0, len(string_num)):
        # number% 10 ** 

