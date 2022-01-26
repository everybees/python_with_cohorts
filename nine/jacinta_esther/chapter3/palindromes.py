number = input("Enter five digits: ")
if range(len(number) == 5):
    # for i in range(len(number)):
    if number[0] == number[4] and number[1] == number[3]:
        print("This number is a palindrome")
    else:
        print("This is not a palindrome number")
else:
    print("invalid length of digit")
