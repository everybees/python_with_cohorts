# from nine.yussuf.arithmetic_ch2 import square_of_a_number
def square_of_a_userInput(number):
    new_Number = int(number)
    square = 1
    if new_Number > 0:
        for i in range (new_Number):
            square = square * new_Number
    return square

user_input = int(input("Enter number:"))
square_of_user_input = square_of_a_userInput(user_input)
addition_of_userInput_and_square = user_input + square_of_user_input
if addition_of_userInput_and_square > 100: print(addition_of_userInput_and_square," is greater than 100")
if addition_of_userInput_and_square < 100: print(addition_of_userInput_and_square,"is less than 100")
if addition_of_userInput_and_square == 100: print(addition_of_userInput_and_square,"is equal to 100")
if addition_of_userInput_and_square != 100: print(addition_of_userInput_and_square,"is not equal to 100")