# for i in range(1, 11):
#     for j in range(0, 1):
#         print("*", end="")
#     for j in range(0, 11-i-1):
# 	    print(" ", end="")
#     for j in range(0, 2*i):
# 	    print(" ", end="")
#     for j in range(0, 11-i):
# 	    print(" ", end="")
#     for j in range(0, 11-i-1):
# 	    print(" ", end="")
#     for j in range(1, i):
#         print("*", end="")
# print()


for i in range(1, 7):
    for j in range(1, i):
        print(j, end="")

    print()
print("\n")

for i in range(6):
    for j in range(5, i, -1):
        print(j, end="")
    print()
