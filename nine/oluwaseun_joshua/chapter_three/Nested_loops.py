for row in range (10):
    for column in range(0,row+1):
        print("*" ,end="")

    
    print()

print()

for row in range (10):
    for column in range(10,row,-1):
        print("*",end="")
    
    print()

for  row in range (10):
    for column in range(0,row,+1):
        print("",end="")
    for column in range(10,row,-1):
        print("*",end="")

    print()

print()

for row in range (10):
    for column in range(10,row,-1):
        print(" ",end="")
    for column in range(0,row,1):
        print("*",end="")

    print()