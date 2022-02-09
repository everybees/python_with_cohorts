# (Odd or Even) Use if statements to determine whether an integer is odd or even.
# [Hint: Use the remainder operator. An even number is a multiple of 2. Any multiple of 2
# leaves a remainder of 0 when divided by 2.]

# ANSWER

user_input = int(input("Enter an integer: "))
if user_input % 2 == 0:
    print(user_input,'is an even number')
else:
    print(user_input,'is an odd number')