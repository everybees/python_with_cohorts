

# for (int row = 0; row < 10; row++) {
#             for (int column = 0; column <= row; column++) {
#                 System.out.print("# ");
#             }
#             System.out.println();
#         }


# row = 0
# column =0

for row in range(1, 6, +1):
    for column in range(1, row +1, +1):
        print(column, end=" ")
    print()


print()


# row = 0
# column =0

for row in range(6, 1, -1):
    for column in range(row -1, 0, -1):
        print(column, end=" ")
    print()

print()

for row in range(6, 1, -1):
    for column in range(row -1, 0, -1):
        print("&", end=" ")
        for i in range(1, 6, row):
            print("$", end=" ")
    print()



