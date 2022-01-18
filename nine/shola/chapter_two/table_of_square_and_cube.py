# (Table of Squares and Cubes) Write a script that calculates the squares and cubes
# of the numbers from 0 to 5. Print the resulting values in table format, as shown below. Use
# the tab escape sequence to achieve the three-column output.
# number square cube
print("number \t square\t cube\t")
for i in range(6):
    print(f'{i} \t\t {i ** 2} \t\t {i ** 3}')

