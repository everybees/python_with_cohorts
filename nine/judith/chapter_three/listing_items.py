a = ["Bananas", "Oranges", "Mangoes"]
b = ["Bread", "Eggs", "Tomatoes"]
c = ["Rice", "Beans", "Yams"]

variables = [a, b, c]

# for col in range(3):
#   for row in range(3):
#      print(variables[row][col], end=' ')

# print()
# for col in range(3):
#     for row in range(3):
#         print(col, row, end=" ", sep='-')  # to print out the positions in a list
#         print(variables[col][row], end=' ')
#         print()

# for row in range(2, -1, -1):
#     for col in range(2, -1, -1):
#         print(variables[row][col])
#         print()
for col in range(2, -1, -1):
    for row in range(2, -1, -1):
        print(variables[col][row])
        print()
