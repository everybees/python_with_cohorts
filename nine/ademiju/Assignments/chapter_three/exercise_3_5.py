# (if…else Statements) Reimplement the script of Fig. 2.1 using three if…else
# statements rather than six if statements. [Hint: For example, think of == and != as “opposite”
# tests.]
number1 = int(input("Enter a number"))
number2 = int(input("Enter a number"))
if(number1>number2):
    print(number1,'is greater than',number2)
else:
    print(number1,'is less than',number2)
if(number1 == number2):
    print(number1,'is equal to',number2)
else:
    print(number1,'is not equal to',number2)
if(number1 >= number2):
    print(number1,'is greater than or equal to',number2)
else:
    print(number1,'is less than or equal to',number2)
