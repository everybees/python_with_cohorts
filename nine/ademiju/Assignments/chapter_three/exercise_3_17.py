# (Nested Loops) Write a script that displays the following triangle patterns separately,
# one below the other. Separate each pattern from the next by one blank line. Use for
# loops to generate the patterns. Display all asterisks (*) with a single statement of the form
# print('*', end='')
# which causes the asterisks to display side by side. [Hint: For the last two patterns, begin
# each line with zero or more space characters.]
# (a)         (i)               (c)               (d)
# *           **********  **********               *
# **          *********    *********              **
# ***         ********      ********             ***
# ****        *******        *******            ****
# *****       ******          ******           *****
# ******      *****            *****          ******
# *******     ****              ****         *******
# ********    ***                ***        ********
# *********   **                  **       *********
# **********  *                    *      **********


for row in range(10):
    for column in range(0, row+1):
       print("*",end="")
    print()
print()
for row in range(10):
    for column in range(10,row,-1):
        print("*",end="")
    print()
print()
for row in range(10):
    for column in range(0,row+1):
        print(' ',end="")
    for column in range(10,row,-1):
          print("*",end="")
    print()
print()
for row in range(10):
    for column in range(10,row,-1):
        print(' ',end="")
    for column in range(0,row+1):
          print('*',end="")
    print()
print() 