
for row in range (1,6,):
    for column in range(1,row +1):
        print(column, end=" ")

    print()

print()




for row in range (5,0,-1):
    for column in range(row,0,-1):
        print(column, end=" ")

    print()

print()


for row in range (1, 6):
    for space in range(1, row):
        print("", end=" ")
    for column in range(row, 6):
        print(column, sep=" ",end="")
    print("\n")
