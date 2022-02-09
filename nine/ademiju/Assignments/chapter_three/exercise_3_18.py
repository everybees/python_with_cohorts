# (Challenge: Nested Looping) Modify your script from Exercise 3.17 to display all
# four patterns side-by-side (as shown above) by making clever use of nested for loops. Separate
# each triangle from the next by three horizontal spaces. [Hint: One for loop should
# control the row number. Its nested for loops should calculate from the row number the
# appropriate number of asterisks and spaces for each of the four patterns.]

for row in range(10):
    for column in range(0,row+1):
        print('*',end="")
    for column in range(10,row,-1):
          print(" ",end="")
    for column in range(10,row,-1):
          print("*",end="")
    for column in range(0,row+1):
        print(' ',end="")
    for column in range(0,row+1):
        print(' ',end="")
    for column in range(10,row,-1):
          print("*",end="")
    for column in range(10,row,-1):
          print(" ",end="")
    for column in range(0,row+1):
        print('*',end="")
    
    print()
