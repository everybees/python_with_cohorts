# star="*"

# for row in range (0,3):
#   for column in range(row):
     
#         print(star,sep="",end=" ")

# print()

# for row in range (1,4):
#     print(star)


# for row in range (1,4):
#     for column in range(1): 
#         print("*",sep=" ",end=" ")

for i in range(1, 5) :
        for j in range(1, 5) :
            if (i == 1 or i == 4 or
                j == 1 or j == 4) :           
                print("*", end = " ")           
            else :
                print(" ", end = " ")           
         
        print()
