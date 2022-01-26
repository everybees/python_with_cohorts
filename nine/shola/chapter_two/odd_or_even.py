# (Odd or Even) Use if statements to determine whether an integer is odd or even.
# [Hint: Use the remainder operator. An even number is a multiple of 2. Any multiple of 2
# leaves a remainder of 0 when divided by 2.]

number = int(input("Enter a number"))
if number % 2 == 0:
    print("Even number")
if number % 2 != 0:
    print("Odd number")
