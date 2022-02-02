a = ['banana','orange','mango']
b = ['bread','eggs','tomato']
c = ['rice','beans','yam']
print('===============================================')
print('SN\t','\tObject\t','\tPosition')
food = [a,b,c]
counter = 0
for column in range(3):
    for row in range(3):
        counter+=1
        print(f'{counter}\t\t{food[row][column]}\t\t{[row]}{[column]}',end=' ')
        print(' ')

print('===============================================')

print('===============================================')
print('SN\t','\tObject\t','\tPosition')
food = [a,b,c]
counter = 0
for row in range(3):
    for column in range(3):
        counter+=1
        print(f'{counter}\t\t{food[row][column]}\t\t{[row]}{[column]}',end=" ")
        print('')

print('===============================================')

print('===============================================')
print('SN\t','\tObject\t','\tPosition')
food = [a,b,c]
counter = 0
for row in range(2, -1,-1):
    for column in range(2,-1,-1):
        counter+=1
        print(f'{counter}\t\t{food[column][row]}\t\t{[column]}{[row]}',end=" ")
        print('')

print('===============================================')

    
