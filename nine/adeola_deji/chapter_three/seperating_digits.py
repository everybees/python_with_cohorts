seperated_digit = ""
number = int(input("Enter digit: "))
string_num = str(number)
for i in range(len(string_num)):
    print (number// 10**(len(string_num)-i))