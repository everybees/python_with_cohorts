# 4.17 (Computer-Assisted Instruction:
# Varying the Types of Problems) Modify the previous exercise to allow the user to pick a type of arithmetic problem
# to study—1 means addition problems only, 2 means subtraction problems only, 3 means multiplication
# problems only, 4 means division problems only (avoid dividing by 0) and 5 means a random mixture of all these types.
import random

value_1 = random.randrange(1, 10)
value_2 = random.randrange(1, 10)


def arithmetica(num):
    if num == 1:
        value = value_1 + value_2
    elif num == 2:
        value = value_1 - value_2
    elif num == 3:
        value = value_1 * value_2
    elif num == 4:
        if value_1 > value_2:
            value = value_1 / value_2
        else:
            value = value_2 / value_1
    elif num == 5:
        integer = random.randrange(1, 5)
        value = integer
    else:
        value = 0
    return value


count = 1
while count <= 10:
    digit = int(input("""Enter a number from 1 to 5: 
    1-for addition problems, 
    2-for subtraction problems, 
    3-for multiplication problems, 
    4-for division problems, 
    5-for a random surprise: 
    """))

    if digit == 1:
        arithmetica(digit)
        print("What is the sum of", value_1, "and",  value_2, "?")
        answer = int(input())
        if answer == arithmetica(digit):
            print("Congratulations! You got the right answer.")
            value_2 = random.randrange(1, 10)
            value_1 = random.randrange(1, 10)
            count += 1
        else:
            print("Incorrect. Try again.")

    if digit == 2:
        arithmetica(digit)
        print("What is the difference between", value_1, "and", value_2, "?")
        answer = int(input())
        if answer == arithmetica(digit):
            print("Congratulations! You got the right answer.")
            value_2 = random.randrange(1, 10)
            value_1 = random.randrange(1, 10)
            count += 1
        else:
            print("Incorrect. Try again.")

    if digit == 3:
        arithmetica(digit)
        print("What is the product of", value_1, "and", value_2, "?")
        answer = int(input())
        if answer == arithmetica(digit):
            print("Congratulations! You got the right answer.")
            value_2 = random.randrange(1, 10)
            value_1 = random.randrange(1, 10)
            count += 1
        else:
            print("Incorrect. Try again.")

    if digit == 4:
        arithmetica(digit)
        print("What is the quotient of", value_1, "and", value_2, "to 2 decimal places?")
        answer = float(input())
        if answer == f'{arithmetica(digit):.2f}':
            print("Congratulations! You got the right answer.")
            value_2 = random.randrange(1, 10)
            value_1 = random.randrange(1, 10)
            count += 1
        else:
            print("Incorrect. Try again.")

    if digit == 5:
        digit = arithmetica(digit)
        if digit == 1:
            arithmetica(digit)
            print("What is the sum of", value_1, "and", value_2, "?")
            answer = int(input())
            if answer == arithmetica(digit):
                print("Congratulations! You got the right answer.")
                value_2 = random.randrange(1, 10)
                value_1 = random.randrange(1, 10)
                count += 1
            else:
                print("Incorrect. Try again.")

        if digit == 2:
            arithmetica(digit)
            print("What is the difference between", value_1, "and", value_2, "?")
            answer = int(input())
            if answer == arithmetica(digit):
                print("Congratulations! You got the right answer.")
                value_2 = random.randrange(1, 10)
                value_1 = random.randrange(1, 10)
                count += 1
            else:
                print("Incorrect. Try again.")

        if digit == 3:
            arithmetica(digit)
            print("What is the product of", value_1, "and", value_2, "?")
            answer = int(input())
            if answer == arithmetica(digit):
                print("Congratulations! You got the right answer.")
                value_2 = random.randrange(1, 10)
                value_1 = random.randrange(1, 10)
                count += 1
            else:
                print("Incorrect. Try again.")

        if digit == 4:
            arithmetica(digit)
            print("What is the quotient of", value_1, "and", value_2, "to 2 decimal places?")
            answer = float(input())
            if answer == f'{arithmetica(digit):.2f}':
                print("Congratulations! You got the right answer.")
                value_2 = random.randrange(1, 10)
                value_1 = random.randrange(1, 10)
                count += 1
            else:
                print("Incorrect. Try again.")


print("You have successfully answered 10 correct questions. \
Congrats! Do go back and look at the places you erred, to get better at them")
