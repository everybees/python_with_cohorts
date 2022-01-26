# 4.16 (Computer-Assisted Instruction: Difficulty Levels) Modify the previous exercise to
# allow the user to enter a difficulty level. At a difficulty level of 1, the program should use
# only single-digit numbers in the problems and at a difficulty level of 2, numbers as large
# as two digits.
import random

value_1 = random.randrange(1, 10)
value_2 = random.randrange(1, 10)
value_3 = random.randrange(1, 100)
value_4 = random.randrange(1, 100)


def product_1():
    value = value_1 * value_2
    return value


def product_2():
    value_ = value_3 * value_4
    return value_


count = 1
while count <= 10:
    if count < 6:
        print("What is the product of", value_1, "and", value_2, "?")
        guess = int(input())
        if guess == product_1():
            print("Congratulations! You got it right")
            count += 1
            value_1 = random.randrange(1, 10)
            value_2 = random. randrange(1, 10)
        elif guess != product_1():
            print("Incorrect. try again")
    if count > 5:
        print("What is the product of", value_3, "and", value_4, "?")
        guess = int(input())
        if guess == product_2():
            print("Congratulations! You got it right")
            count += 1
            value_3 = random.randrange(1, 100)
            value_4 = random.randrange(1, 100)
        elif guess != product_2():
            print("Incorrect. try again")