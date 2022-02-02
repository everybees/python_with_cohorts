


# def greet():
#     x=10
#     print("value inside function: ",greet(x))


# # function overload in python
# def addition(number1,number2,number3,number4=0):
#     return number1+number2+number3+number4

# print(addition(2,3,4))


import string


def free_flow(a_str='',an_int=0, a_float=0.0, a_list=[],a_dict ={}):
    if a_str:
        print(a_str)
        print(an_int)
        print(a_float)
        print(type(a_str))
    else:
        print("Nothing was entered!")

# free_flow("goat",1.0, "hen")
free_flow(1,[2,3,4],8.0)
free_flow(an_int=1,a_list=[2,3,4],a_float=5.4,a_str="joshua")


    

    
    







