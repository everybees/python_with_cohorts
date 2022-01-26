# (7% Investment Return) Reimplement Exercise 2.12 to use a loop that calculates
# and displays the amount of money you’ll have each year at the ends of years 1 through 30.


p = 1000
r = 0.7
for i in range(10, 40, 10):
    investment_return = 1000 * (1 + 0.7) * i
    print(investment_return)
