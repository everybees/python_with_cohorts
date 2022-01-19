variable = [['Banana', 'Oranges', 'Mangoes'], ['Bread', 'Eggs', 'Tomatoes'], ['Rice', 'Beans', 'Yams']]

for col in range(3):
    for row in range(3):
        print(col, row, end=' ', sep='-')
        print(variable[col][row])

print("\n")

for row in range(2, -1, -1):
    for col in range(2, -1, -1):
        print(col, row, end=' ', sep='-')
        print(variable[row][col])
print('\n')

for row in range(2, -1, -1):
    for col in range(2, -1, -1):
        print(col, row, end=' ', sep='-')
        print(variable[col][row])




#row = 2
#while row >= 0:
#col = 2
#while col >= 0:
  #    print(row, col, end=' ', sep='-')
 #     print(variable[row][col])
#col = col - 1
#row = row - 1