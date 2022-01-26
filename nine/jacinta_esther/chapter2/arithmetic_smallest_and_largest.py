import sys

maximum = 0
sum = 0
product = 1
minimum = sys.maxsize

for i in range(3):
    number = int(input("Enter a number: "))
    sum += number
    product *= number

    if number > maximum: maximum = number
    if number < minimum: minimum = number

print("The largest number is ", maximum)
print("The smallest number is: ", minimum)
print("The sum is: ", sum)
print("The product is: ", product)
print("the average is: ", sum / 3)
