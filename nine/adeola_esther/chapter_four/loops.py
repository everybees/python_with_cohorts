

for row in range(0, 11 ):
    for column in range(0, row):
        print( '*', end=" " )
    print()
print ()
for row in range(0, 11):
    for column in range(11, row, -1):
        print( '*', end=" ")
    print()
print()
for row in range(11, 0):
    for column in range(1, row ,11):
        print( '*', end=" ")
    print()
print()

# 
   
