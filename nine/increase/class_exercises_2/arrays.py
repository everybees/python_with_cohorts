a = ['Bananas','Orange','Mangoes']
b = ['Bread', 'Eggs','Tomatoes']
c = ['Rice','Beans','Yams']

variable = [a,b,c]

# print(variable)

count = 0
for column in range(3):
    for row in range(3):
        count+=1
        print(count, end=' ') 
        print(row,column, end=' ', sep=' ')
        # print(variable[column] [0], end=' ')
        print(variable[row][column], row, column)

print()

for row in range(2,-1,-1):
    for column in range(2,-1,-1):
        print(variable[row][column],row,column)

print()

for row in range(2,2):
    for column in range(2,2):
        print(variable[row][column],row,column)
        
        
    