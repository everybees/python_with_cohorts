def function_with_two_parameters(first_name, last_name):
    print(first_name + " " + last_name)

def age(current_year, year_born):
    age = current_year - year_born
    print(age)

def square(number):
    result = number * number
    print(result)

def user(first_name):
    print(first_name + "David")


def addition(no1, no2, no3, no4, no5):
    return no1 + no2 + no3 + no4 + no5

def freeflow(a_string = " ", an_int = 0, a_float = 0.0, a_list = [], a_dict = {}):
    print(a_list, a_string)

freeflow("Welcome", [2, 6, 7, 100])

