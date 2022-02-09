listing=[
    ["Bananas","Bread", "Rice",], 
    ["Eggs","Oranges","Beans"], 
    ["Mangoes","Tomatoes" ,"Yams"]
]

print(1, listing[0][0],  0, 0)
print(2, listing[0][1],   0, 1)
print(3, listing[0][2],  2, 0)
print(4, listing[0][0],   0, 1)
print(5, listing[1][0],  1, 1)
print(6, listing[1][1],  2, 1)
print(7, listing[1][2],  0,  2)
print(8, listing[2][0],   2,  1)
print(9,  listing[2][1],  2,  2 )
print()




print(1, listing[2][2],  2, 2)
print(2, listing[2][1],   2, 1)
print(3, listing[0][2],   0, 2)
print(4, listing[2][1],   2, 1)
print(5, listing[1][1],  1, 1)
print(6, listing[0][1],  0, 1)
print(7, listing[2][0],  2,  0)
print(8, listing[1][0],   1,  0)
print(9,  listing[0][0],  0,  0 )
print()



print(1, listing[0][0],  0, 0)
print(2, listing[1][1],   1, 1)
print(3, listing[2][0],  2, 0)
print(4, listing[1][1],   1, 1)
print(5, listing[2][1],  2, 1)
print(6, listing[2][2],  2, 2)
print(7, listing[2][0],  2,  0)
print(8, listing[0][2],   0,  2)
print(9,  listing[2][2],  2,  2 )
print()

count=0

for column in range(2, -1, -1):
    for row in range(2, -1, -1):
        
        print(listing[row][column], end="\t")
        print(row, column, end="\n")

print()    

for row in range(2, -1, -1):
    for column in range(2, -1, -1):
    

        print(listing[row][column], end="\t")
        print(row, column, end="\n")

print()    