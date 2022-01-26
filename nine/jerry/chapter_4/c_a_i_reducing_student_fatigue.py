# 4.15 (Computer-Assisted Instruction: Reducing Student Fatigue)
# Varying the computer’s responses can help hold the student’s attention. Modify the previous exercise so that
# various comments are displayed for each answer. Possible responses to a correct answer
# should include 'Very good!', 'Nice work!' and 'Keep up the good work!'
# Possible responses to an incorrect answer should include 'No. Please try again.', 'Wrong. Try once more.'
# and 'No. Keep trying.' Choose a number from 1 to 3, then use that value
# to select one of the three appropriate responses to each correct or incorrect answer.
import random

value1 = random.randrange(1, 10)
value2 = random.randrange(1, 10)



def product():
    value = value2 * value1
    return value


correct_answer = product()
count = 0
while count != 1:
    value3 = random.randrange(1, 4)
    print("What is the product of", value1, "and", value2, "?")
    answer = int(input())
    if answer == correct_answer:
        if value3 == 1: print("Very good!")
        elif value3 == 2: print("Nice work!")
        elif value3 == 3: print("Correct! Keep up the good work!")
        count += 1
    else:
        if value3 == 1: print("No. Please try again")
        elif value3 == 2: print("Wrong. Try once more")
        elif value3 == 3: print("No, keep trying")

