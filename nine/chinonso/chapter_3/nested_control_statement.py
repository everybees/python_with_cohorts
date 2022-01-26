import sys

counter = 0
mini = sys.maxsize
maxi = -sys.maxsize
for j in range(10):
    number = int(input('Enter number :'))
    counter += 1
    if number > maxi:
        maxi = number
    if number < mini:
        mini = number
print('the Largest is ', maxi)
print('the smallest is ', mini)
