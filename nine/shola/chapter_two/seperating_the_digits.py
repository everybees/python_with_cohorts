# (Separating the Digits in an Integer) Write a script that inputs a five-digit integer
# from the user. Separate the number into its individual digits. Print them separated by three
# spaces each. For example, if the user types in the number 42339, the script should print 4 2 3 3 9

separator = input("Enter a five digit number")
if len(separator) == 5:
    num1 = int(separator) // 10000
    num2 = int(separator) % 10000 // 1000
    num3 = int(separator) % 1000 // 100
    num4 = int(separator) % 100 // 10
    num5 = int(separator) % 10
    print(num1, "   ", num2, "   ", num3, "   ", num4, "   ", num5)
else:
    print("excess number")
