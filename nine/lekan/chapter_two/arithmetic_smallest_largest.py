import sys

sum = 0

average = 0
product = 1
smallest = sys.maxsize
largest = 0
count = 0

for i in range(3):
    user_input = int(input('Enter A Number: '))

    count += 1

    sum += user_input
    product *= user_input

    if smallest > user_input:
        smallest = user_input
    if largest < user_input:
        largest = user_input

average = sum / count
print("The sum is ", sum)
print("The average is ", average)
print("The product is ", product)
print("The smallest value is ", smallest)
print("The largest value is ", largest)
