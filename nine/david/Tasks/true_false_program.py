# Write a program that returns true or false if the input value is equal or not equal to the default value

default_value = 10
user = input("Enter an input")
user_input = int(user)

if user_input == default_value:
    print("True")
else:
    print("False")