# Author: Joshua
# Title :3.8

maximum = 0
minimum = 100
total = 0
average = 0

for grade in range(4):
    score = int(input("Input score"))
    grade = grade+1

    total = total + score
    average = total / grade

    if maximum < score:
        maximum = score

    if score < minimum:
        minimum = score

print(total)
print(average)
print(maximum)
print(minimum)
