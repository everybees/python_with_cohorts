from curses.ascii import US
from re import U


user_input = int(input("Enter digit: "))
for row in range(1, user_input+1):
    for column in range(0, row):
        print("* ", end="")
    print()

print()

for row in range(user_input+1, 0, -1):
    for column in range(1, row):
        print("* ", end="")
    print()

print()

for row in range(user_input, 0, -1):
    for index in range(row, user_input):
        print("  ", end="")
    for column in range(1, row+1):
        print(" *", end="")
    
    print()

print()

for i in range(1, user_input+1):
    for j in range(user_input, i, -1):
        print("  ", end="")
    for k in range(i, 0, -1):
        print("* ", end="")
    print()    