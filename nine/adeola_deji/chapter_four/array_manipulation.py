from os import sep


fruits = [["banana", "orange", "mangoes"], 
          ["bread", "eggs", "tomatoes"], 
          ["rice", "beans", "yam"]]

count =0
for i in range(len(fruits)):
    for j in range(1):
        count+=1
        print(count, end=". ")
        # print()
        print( i, j, end=" ", sep="-")
        print(fruits[i][0], end=" ")
    print()
# print()
for i in range(len(fruits)):
    for j in range(1, 2):
        count+=1
        print(count, end=". ")
        print( i, j, end=" ", sep="-")
        print(fruits[i][j], end=" ")
    print()
# print()

for i in range(len(fruits)):
    for j in range(2,3):
        count+=1
        print(count, end=". ")
        print(i, j, end=" ", sep="-")
        print(fruits[i][j], end=" ")
    print()
print()

for i in range(len(fruits)):
    for j in range(len(fruits[i])):
        print(fruits[i][j], end=" ")
    print()
print()
print()


for i in range(len(fruits)):
    for j in range(len(fruits[i])):
        print(fruits[i][j])
    print()
print()

for i in range(len(fruits)-1, -1, -1):
    for j in range(len(fruits[i])-1, -1, -1):
        print(fruits[i][j], end="  ")
    print()
print()

for i in range(len(fruits)-1, -1, -1):
    for j in range(len(fruits[i]), 3):
        print(fruits[i][j], end=" ")
    print()