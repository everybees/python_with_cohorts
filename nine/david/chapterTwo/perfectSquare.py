import math
user_number = int(input("Enter a number: "))

square_root = math.sqrt(user_number)

if int(square_root + 0.5) ** 2 == user_number:
    print(user_number, "is a perfect square")
else:
    print(user_number, "is not a perfect square")
