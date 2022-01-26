x = ["Banana", "Orange", "Mangoes"]
y = ["Bread", "Eggs", "Tomatoes"]
z = ["Rice", "Beans", "Yams"]


food = [x, y, z]

for column in range(3):
    for row in range(3):
        print(food[row][column], end=" ")
    print()


print("\n")

count = 0
for column in range(3):
    for row in range(3):
        count += 1
        print(count, end="\t")
        print(food[row][column], end="\t")
        print(row, column, end="\n")

print("\n")

counter = 0
for column in range(2, -1, -1):
    for row in range(2, -1, -1):
        counter += 1
        print(counter, end="\t")
        print(food[row][column], end="\t")
        print(row, column, end="\n")

print("\n")

integer = 0
for row in range(2, -1, -1):
    for column in range(2, -1, -1):
        integer += 1
        print(integer, end="\t")
        print(food[row][column], end="\t")
        print(row, column, end="\n")