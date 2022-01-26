a = ["Banana", "Oranges", "Mangoes"]
b = ["Bread", "Eggs", "Tomatoes"]
c = ["Rice", "Beans", "Yams"]

food_stuff = [a, b, c]
print(a[0], end=" ")
print(a[1], end=" ")
print(a[2], end="\n")
print(b[0], end=" ")
print(b[1], end=" ")
print(b[2], end="\n")
print(c[0], end=" ")
print(c[1], end=" ")
print(c[2], end="\n")

serial_number = 0
for row in range(3):
    for column in range(3):
        serial_number += 1
        print(serial_number, end="\t")
        print(food_stuff[row][column], end="\t")
        print(row, column, end="\n")
print()
count = 0
for column in range(2, -1, -1):
    for row in range(2, -1, -1):
        count += 1
        print(count, end="\t")
        print(food_stuff[row][column], end="\t")
        print(row, column, end="\n")

print()
cunt = 0
for row in range(2, -1, -1):
    for column in range(2, -1, -1):
        cunt += 1
        print(cunt, end="\t")
        print(food_stuff[row][column], end="\t")
        print(row, column, end="\n")
