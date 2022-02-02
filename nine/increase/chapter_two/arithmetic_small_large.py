# (Arithmetic, Smallest and Largest) Write a script that inputs three
# integers from the user. Display the sum, average, product, smallest and
# largest of the numbers. Note that each of these is a reduction in functional-
# style programming.

user_input1= int(input('Enter an integer: '))
user_input2= int(input('Enter an integer: '))
user_input3= int(input('Enter an integer: '))

sum = user_input1 + user_input2 + user_input3
average = sum / 3
product = user_input1 * user_input2 * user_input3
smallest = min(user_input1,user_input2, user_input3)
largest = max(user_input1,user_input2,user_input3)

print('The sum is :',sum ,'\n The average is :',average ,'\n The product is :', product ,
'\n The smallest is :', smallest, '\n The largest is :',largest )