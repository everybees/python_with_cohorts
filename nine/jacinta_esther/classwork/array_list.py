variable = [['Banana', 'Orange', 'Mango'], ['Bread', 'Egg', 'Tomato'], ['Rice', 'Beans', 'Yam']]

serial_number = 1
for row in range(3):
    for column in range(3):
        print(serial_number, end="  ")
        print(row, column, end=" ", sep="-")
        print(variable[row][column])
        serial_number += 1
print()
serial_number = 1
for row in range(2, -1, -1):
    for column in range(2, -1, -1):
        print(serial_number, end="  ")
        print(row, column, end=" ", sep="-")
        print(variable[row][column])
        serial_number += 1
print()
serial_number = 1
for row in range(2, -1, -1):
    for column in range(2, -1, -1):
        print(serial_number, end="  ")
        print(row, column, end=" ", sep="-")
        print(variable[column][row])
        serial_number += 1
