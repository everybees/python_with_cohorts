# 3.18 (Challenge: Nested Looping) Modify your script from Exercise 3.17 to display all
# four patterns side-by-side (as shown above) by making clever use of nested for loops.
# Separate each triangle from the next by three horizontal spaces. [Hint: One for loop should
# control the row number. It's nested for loops should calculate from the row number the
# appropriate number of asterisks and spaces for each of the four patterns.]


count = 0
for t in range(1):
    for i in range(1, 11):
        for j in range(i):
            print("*", end="")
        for y in range(12 - i):
            print("", end=" ")
        for k in range(1, 12-i):
            print("*", end="")
        for a in range(1*i+count):
            print("", end=" ")
        count += 1
        for b in range(11-i, 0, -1):
            print("*", end="")
        for e in range(i, 11):
            print("", end=" ")
        for r in range(i):
            print("*", end="")
        print()
