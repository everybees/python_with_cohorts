# (What’s wrong with this code?) The following code should read an integer into the
# variable rating:
# rating = input('Enter an integer rating between 1 and 10')

# ANSWER
# input function takes in a String data types except otherwise declared
# to take an integer input it can be written instead as:
# rating = int(input('Enter an integer rating between 1 and 10'))