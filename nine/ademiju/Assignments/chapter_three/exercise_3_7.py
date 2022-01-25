# (Table of Squares and Cubes) In Exercise 2.8, you wrote a script to calculate the
# squares and cubes of the numbers from 0 through 5, then printed the resulting values in
# table format. Reimplement your script using a for loop and the f-string capabilities you
# learned in this chapter to produce the following table with the numbers right aligned in
# each column.
# number square cube
#      0      0    0
#      1      1    1
#      2      4    8
#      3      9   27
#      4     16   64
#      5     25  125

print("number","\tsquare","\tcube")
for number in range (6):
    square = number**2
    cube = number**3
    print(f"{number:>6}{square:>8}{cube:>6}")