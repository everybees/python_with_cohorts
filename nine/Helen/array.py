a = ["banana", "orange", "mango"]
b= ["bread", "eggs", "tomatoe"]
c = ["rice", "beans", "yam"]
variable = [a, b, c]
counter = 0
# for col in range(3):
#     for row in range(3):
#         counter +=1
#         print(counter, variable[row][col], row, col)

# for col in range(3):
#     for row in range(3):
#         counter +=1
#         print(counter, variable[col][row], row, col)

row = 2
while row >= 0:
    col = 2
    while col >= 0:
        print(variable[col][row])
        col -= 1
    row -= 1

