userInput = int(input("Enter number "))
print("Number\tSquare\tCube")

for i in range(1,userInput):
    square = i * i
    cube = square * i
    print(i,"\t",square,"\t",cube)