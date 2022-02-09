# 1
# 1   2
# 1   2   3   
# 1   2   3   4
# 1   2   3   4   5

# 5   4   3   2   1
# 5   4   3   2
# 5   4   3
# 5   4
# 5


for row in range (1,6):
    for column in range(1,row+1):
        print(column, end=" " )
    print(' ')

print()

for row in range(0,6):
    for column in range(5,row, -1):
        print(column, end=" ")
    print(' ')