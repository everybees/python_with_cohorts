for number_row in range(1, 7):
    for number_column in range(1, number_row):
        print(number_column, end=" ")
    print()

for number_row in range(6):
    for number_column in range(5,number_row, -1):
        print(number_column, end=" ")
    print()
