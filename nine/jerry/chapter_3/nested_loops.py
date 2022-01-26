# 3.17 (Nested Loops) Write a script that displays the following triangle patterns separately, one below the other.
# Separate each pattern from the next by one blank line. Use for loops to generate the patterns.
# Display all asterisks (*) with a single statement of the form print('*', end='')
# which causes the asterisks to display side by side. [Hint: For the last two patterns, begin
# each line with zero or more space characters.]


for i in range(1, 11):
    for j in range(i):
        print("*", end="")
    print("\n")


count = 11
while count >= 1:
    for k in range(1, count+1):
        if count < 11:
            print("*", end="")
    print("\n")
    count -= 1


for p in range (1, 11):
    for q in range(1, p):
        print("", end=" ")
    for r in range(p, 11):
        print("*", end="")

    print("\n")

for x in range(1, 11):
    for y in range(x, 10):
        print("", end=" ")
    for z in range(1, x+1):
        print("*", end="")
    print("\n")


