user_input = int(input("Enter a number"))
factorial = 1
for i in range(user_input):
    factorial *= user_input
    user_input -= 1
print("The factorial is", factorial)
