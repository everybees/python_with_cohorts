# (Table of Squares and Cubes) In Exercise 2.8, you wrote a script to calculate the
# squares and cubes of the numbers from 0 through 5, then printed the resulting values in
# table format. Reimplement your script using a for loop and the f-string capabilities you
# learned in this chapter to produce the following table with the numbers right aligned in
# each column.


print(f'number\tsquare\tcube')

number = 5
for numbers in range(0,6):
    print(f' {numbers} \t {numbers * numbers} \t {numbers * numbers * numbers}')