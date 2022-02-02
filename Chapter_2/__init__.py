# (What does this code do?) Create the variables x = 2 and y = 3, then determine what
# each of the following statements displays:
# a) print('x =', x)
# b) print('Value of', x, '+', x, 'is', (x + x))
# c) print('x =')
# d) print((x + y), '=', (y + x))


x = 2
y = 3

print('x =', x)
print('Value of', x, '+', x, 'is', (x + x))
print('x =')
print((x + y), '=', (y + x))

print()
# What’s wrong with this code?) The following code should read an integer into the
# variable rating:
# rating = input('Enter an integer rating between 1 and 10')

rating = int(input('Enter an integer rating between 1 and 10'))


print()
# (Fill in the missing code) Replace *** in the following code with a statement that
# will print a message like 'Congratulations! Your grade of 91 earns you an A in this
# course'. Your statement should print the value stored in the variable grade:
# if grade >= 90:
#  ***

grade = int(input("Input Grade: "))
if grade >= 90:
    print('Congratulations! Your grade of 91 earns you an A in this course')


print()
# (Arithmetic) For each of the arithmetic operators +, -, *, /, // and **, display the
# value of an expression with 27.5 as the left operand and 2 as the right operand.

print(27.5 + 2)
print(27.5 - 2)
print(27.5 * 2)
print(27.5 / 2)
print(27.5 // 2)
print(27.5 * 2)

