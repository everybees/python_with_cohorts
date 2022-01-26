# 3.10 (7% Investment Return) Reimplement Exercise 2.12 to use a loop that calculates
# and displays the amount of money you’ll have each year at the ends of years 1 through 30.
import math

principal = 1000
for year in range(1, 31):
    amount = principal * math.pow(1 + 7, year)
    print("The amount after Year", year, " is", amount)
