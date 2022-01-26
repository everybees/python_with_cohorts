digit = int (input("Enter a five digit integer: "))
a = digit // 10000
b = digit % 10000 //1000
c = digit % 1000 //100
d = digit % 100 //10
e = digit % 10


if a == e and b == d:
    print (f'{digit} is a palindrome of five digits')
else:
    print (f'{digit} is  not a palindrome of five digits')


#to check for palindrome of any number of digits
# digit = input("Enter a five digit integer: ")
# if range(len(digit) == 5):
#     # for i in range(len(digit)):
#     if digit[0] == digit[4] and digit[1] == digit[3]:
#         print("This number is a palindrome")
#     else:
#         print("This is not a palindrome number")
# else:
#     print("incorrect length of digit")