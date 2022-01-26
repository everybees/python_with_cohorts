# 4.14 (Computer-Assisted Instruction) Computer-assisted instruction (CAI) refers to the
# use of computers in education. Write a script to help an elementary school student learn
# multiplication. Create a function that randomly generates and returns a tuple of two positive one-digit integers.
# Use that function’s result in your script to prompt the user with a
# question, such as
# How much is 6 times 7?
# For a correct answer, display the message "Very good!" and ask another multiplication
# question. For an incorrect answer, display the message "No. Please try again." and let
# the student try the same question repeatedly until the student finally gets it right.
import random

value1 = random.randrange(0, 10)
value2 = random.randrange(0, 10)

number = value1, value2


def product():
    value = value2 * value1
    return value


correct_answer = product()
count = 0
while count != 1:
    print("What is the product of", value1, "and", value2, "?")
    answer = int(input())
    if answer == correct_answer:
        print("Very good!")
        count += 1
    else:
        print("No. Please try again")

