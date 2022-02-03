# (Sort in Ascending Order) Write a script that inputs three different floating-point
# numbers from the user. Display the numbers in increasing order. Recall that an if state-
# ment’s suite can contain more than one statement. Prove that your script works by run-
# ning it on all six possible orderings of the numbers. Does your script work with duplicate
# numbers? [This is challenging. In later chapters you’ll do this more conveniently and with
# many more numbers.]

user_input1 = float(input('Enter a number: '))
user_input2 = float(input('Enter a second number: '))
user_input3 = float(input('Enter a third number: '))

if(user_input1 > user_input2 and user_input1 > user_input3):
    if(user_input2 > user_input3):
             print('The increasing order is : ', user_input3,user_input2,user_input1)

if(user_input1 > user_input2 and user_input1 > user_input3):
    if(user_input3 > user_input2):
             print('The increasing order is : ', user_input2,user_input3,user_input1)

if(user_input2 > user_input1 and user_input2 > user_input3):
    if(user_input1 > user_input3):
        print('The increasing order is : ', user_input3,user_input1,user_input2)

if(user_input2 > user_input1 and user_input2 > user_input3):
    if(user_input3 > user_input1):
        print('The increasing order is : ', user_input1,user_input3,user_input2)

if(user_input3 > user_input1 and user_input3 > user_input2):
    if(user_input2 > user_input1):
        print('The increasing order is : ', user_input1,user_input2,user_input3)

if(user_input3 > user_input1 and user_input3 > user_input2):
    if(user_input1 > user_input2):
        print('The increasing order is : ', user_input2,user_input1,user_input3)



