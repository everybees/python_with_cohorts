a = ["Bananas", "Oranges", "Mangoes"]
b = ["bread", "eggs", "tomatoes"]
c = ["rice", "beans", "yam"]

variable = [a, b, c]
print("s/n", "\t fruits", "\t positions")
print()
counter = 0

# for column in range(3):
#     for row in range(3):
#         counter += 1
#         

# for row in range(3):
#     for column in range(3):
#         counter += 1
#         print(f'{counter} \t   {variable[row][column]}  \t   {[row]} {[column]}')
#     # print()


row = 2
while row >= 0:
    col = 2
    while col >= 0:
        print(f'{counter} \t   {variable[col][row]}  \t   {[col]} {[row]}')
        # print(variable[col][row], col, row)
        col -= 1
    row -=1
        
