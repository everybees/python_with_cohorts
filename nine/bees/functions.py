def factorial(number):
    factorial = 1
    for i in range(1, number+1):
        factorial *= i
    return factorial


def addition(number1, number2, number3, number4=0, number5=0):
    return number1 + number2 + number3 + number4 + number5


def subtraction(number1,number2):
    return number1 - number2


def division(number1,number2):
    return number1 / number2


def promise(something="As long as i'm still in Semicolon,I will disturb Semicolon especially Chibuzor"):
    print(something)


def free_flow(a_string="--", an_int=0, a_float=0.0, a_list=[], a_dict={}):
    print(a_list)


free_flow(1, [2, 4, 6], 8.0)
free_flow(an_int=1, a_list=[2, 4, 6], a_float=8.0, a_string="Joshua")
