# def factorial(n):
#
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# def main():
#     user_input = int(input('Enter A Number'))
#     factorial(user_input)
#     print('')





# user_input = int(input('Enter A Number'))
# temp = user_input
# product = 1
# if user_input <= 1:
#     product = 1
# for i in range(temp):
#     product *= temp
#     temp -= 1
# print('The factorial of ', user_input, 'is ', product)

num = int(input("Enter a number:"))

factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
        print("The factorial of", num, "is", factorial)
