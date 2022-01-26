

a = ["Banana", "Oranges", "Mangoes"]
b = ["Bread", "Eggs", "Tomatoes"]
c = ["Rice", "Beans", "Yams"]

food_items = [a, b, c]

for column in range(len(food_items)):
    for row in range(len(food_items[column])):
        print(food_items[row][column], end=" ")
    print()
print()

num = 0
for column in range(3):
    for row in range(3):
        num = num + 1
        print("(",num,")", food_items[row][column], row, column)
print()

# THIS IS THE NORMAL TABLE ARRANGEMENT
for row in range(3):
    for column in range(3):
        print(food_items[row][column], end=" ")
    print()
print()


for row in range(2, -1, -1):
    for column in range(2, -1, -1):
        print(food_items[row][column], end=" ")
    print()
print()

for row in range(2, -1, -1):
    for column in range(2, -1, -1):
        print(food_items[column][row], end=" ")
    print()
print()
