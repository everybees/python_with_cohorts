

from typing import Counter


r=["Bananas","Oranges","Mangoes"]
o=["Bread","Eggs","Tomatoes"]
t=["Rice","Beans","Yams"]

fruit=[r,o,t]
Counter=0


# for row in range (len(fruit)-1, -1,-1):
#     for column in range(0,3):
        
#         print(fruit[row][column], [row],[column],sep="-")


# for index 2
# for row in range (len(fruit)-1,3):
#     for column in range(3):
#         print(fruit[row][column],[row],[column],sep=" ")


# print()

# for row in range (len(fruit)-1,3):
#     for column in range(1):
#         print(fruit[row][column],[row][column],sep=" ")
    
print("s/n \t ")
row=2
while row >= 0:
    column = 2
    while column >=0:
        Counter +=1
        print(f"{Counter} \t   {fruit[column][row]}  \t    {[column]} {[row]}")

        column -=1
    row -=1

