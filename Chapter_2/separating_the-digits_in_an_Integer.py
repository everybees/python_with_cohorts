


# Separating the Digits in an Integer) Write a script that inputs a five-digit integer
# from the user. Separate the number into its individual digits. Print them separated by three
# spaces each. For example, if the user types in the number 42339, the script should print
# 4 2 3 3 9
# Assume that the user enters the correct number of digits. Use both the floor division and
# remainder operations to “pick off” each digit.


number = int(input("Enter five digits: "))

digit1 = number // 10000
digit2 = number % 10000 // 1000
digit3 = number % 10000 % 1000 // 100
digit4 = number % 10000 % 1000 % 100 // 10
digit5 = number % 10000 % 1000 % 100 % 10

print(digit1,digit2,digit3,digit4,digit5, sep="   ")