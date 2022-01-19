variable = [['Banana', 'Orange', 'Mangoes'], ['Bread', 'Eggs', 'Tomatoes'],
            ['Rice', 'Beans', 'Yams']]
print("s/n \t Position \tObject")
serial_number = 0
for col in range(3):
    for row in range(3):
        serial_number += 1
        print(serial_number, end="         ")
        print(col, row, end='       ', sep='-')
        print(variable[col][row])

print()
serial_number = 0
print("s/n \t Position \tObject")

for row in range(2, -1, -1):
    for column in range(2, -1, -1):
        serial_number += 1
        print(serial_number, end="         ")
        print(row, column, end="       ", sep='-')
        print(variable[row][column])
print()

serial_number = 0
print("s/n \t Position \tObject")
for column in range(2, -1, -1):
    for row in range(2, -1, -1):
        serial_number += 1
        print(serial_number, end="         ")
        print(row, column, end="       ", sep='-')
        print(variable[row][column])

name  = "Fola"

    