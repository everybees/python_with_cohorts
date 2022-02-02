
# my first trial code for palindrome in python
# entry = int(input("Enter your five digit integer here: "))

# if (entry // 10000 == 0):
#     print("The number you entered is a palindrome")
# else:
#     print("The number you entered is not a palindrome")


entry = input("Enter your five digit number here: ")

if entry == entry[::-1]:
    print("This number is a palindrome")
else:
    print("This number is not a palindrome")
