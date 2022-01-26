# (Arithmetic, Smallest and Largest) In Exercise 2.10, you wrote a script that input
# three integers, then displayed the sum, average, product, smallest and largest of those values.
# Reimplement your script with a loop that inputs four integers.

from audioop import minmax
from sys import maxsize


sum = 0
product = 1
maximum = 0
minimum =maxsize
for i in range(4):
    user_input = int(input("Enter a number \n"))
    sum += user_input
    product*=user_input
    if(user_input > maximum):
        maximum = user_input
    if(user_input < minimum):
        minimum = user_input


average = sum/4
print("sum =",sum,"\nproduct =",product,"\naverage =",average,"\nmaximum =",maximum,"\nminimum =",minimum,maxsize)