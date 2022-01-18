user_input = int(input('Enter A Number: '))
product = 1

if user_input <= 1:
    product = 1
for i in range(user_input):
    product *= user_input
    user_input -= 1

print("The factorial is ", product)

