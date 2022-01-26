# (Arithmetic, Smallest and Largest) In Exercise 2.10, you wrote a script that input
# three integers, then displayed the sum, average, product, smallest and largest of those val-
# ues. Reimplement your script with a loop that inputs four integers.

for i in range(4):
    user_input=(int(input("Enter an integer : ")))

sum = user_input + user_input + user_input + user_input
average = sum / 4
product = sum * 4
smallest = min(user_input,user_input,user_input,user_input)
largest = max(user_input,user_input,user_input,user_input)


print('The sum is :',sum ,'\n The average is :',average ,'\n The product is :', product ,
'\n The smallest is :', smallest, '\n The largest is :',largest )