#2.1
#answer
# x = 2
# y = 3
# print('x =', x)
# print('Value of', x, '+', x, 'is', (x + x))
# print('x =')
# print((x + y), '=', (y + x))

#2.2
#(What’s wrong with this code?) The following code \
# should read an integer into the variable rating :

#rating = input('Enter an integer rating between 1 and 10: ')

#The code is not reading an integer because inputs read \
# strings and it needs to be casted to int as in:
#Answer
# rating =  int(input('Enter an integer rating between 1 and 10'))

#2.3
#(Fill in the missing code) Replace *** in the following code with a statement that
# will print a message like 'Congratulations! Your grade of 91 earns you an A in this
# course' . Your statement should print the value stored in the variable grade :
# if grade >= 90:
# ***
# Answer
# grade = 91
# if grade >= 90:
#     print("Congratulations! Your grade of ", grade, " earns you an A in this course")

#(Arithmetic) For each of the arithmetic operators + , - , * , / , // and ** , display the
#value of an expression with 27.5 as the left operand and 2 as the right operand.

add_operator = 27.5 + 2
print(add_operator)
print()

subtraction_operator = 27.5 - 2
print(subtraction_operator)
print()

multiplication_operator = 27.5 * 2
print(multiplication_operator)
print()

true_division_operator = 27.5 / 2
print(true_division_operator)
print()

floor_division_operator = 27.5 // 2
print (floor_division_operator)
print()

exponential_operator = 27.5 ** 2
print(exponential_operator)
print()