seperated_digit = ""
number = 1234
string_num = str(number)
for i in range(len(string_num)):
    print (number// (10**(len(string_num)-i))+1 % (10**i*1+1))