# (Table of Squares and Cubes) Write a script that calculates the squares and cubes
# of the numbers from 0 to 5. Print the resulting values in table format, as shown below. Use
# the tab escape sequence to achieve the three-column output.
# number square cube
# 0 0 0
# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64
# 5 25 125


print("N\t\t N2\t\t\t N3")

for i in range(6):
    print(i,"\t\t ",(i ** 2),"\t\t ",(i ** 3))