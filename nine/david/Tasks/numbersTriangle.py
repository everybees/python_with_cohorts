# for row in range(1, 6 + 1):
#     for column in range(1, row + 1):
#         print(column, end=" ")
#     print(" ")



for row in range(0, 5 + 1):
    for column in range(row - 1, 0, -1):
        print(column, end=" ")
    print(" ")

