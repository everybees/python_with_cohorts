# (Arithmetic, Smallest and Largest) Write a script that inputs three integers from
# the user. Display the sum, average, product, smallest and largest of the numbers. Note that
# each of these is a reduction in functional-style programming.

first_number = int(input('Enter first integer: '))
second_number = int(input('Enter second integer: '))
third_number = int(input('Enter third integer: '))

print ('The sum of the numbers is',first_number + second_number + third_number)
print('The average of the number is',(first_number + second_number + third_number )/ 3)
print('The product of the numbers is', (first_number * second_number * third_number))
print('The largest number is', max(first_number, second_number, third_number))
print('The smallest number is',min(first_number, second_number, third_number))