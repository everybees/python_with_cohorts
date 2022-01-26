# (Separating the Digits in an Integer) Write a script that inputs a five-digit integer
# from the user. Separate the number into its individual digits. Print them separated by three
# spaces each. For example, if the user types in the number 42339, the script should print
# 4 2 3 3 9
# Assume that the user enters the correct number of digits. Use both the floor division and
# remainder operations to “pick off ” each digit.


user_input = int(input("Enter a five digit number: "))
last_number = user_input % 10
remainder = user_input // 10
fourth_number = remainder % 10
remainder1= remainder // 10
third_number = remainder1 % 10
remainder2 = remainder1 // 10
second_number = remainder2 % 10
first_number = remainder2//10
print(first_number,'\t',second_number,'\t',third_number,'\t',fourth_number,'\t',last_number)
