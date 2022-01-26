# (7% Investment Return) Reimplement Exercise 2.12 to use a loop that calculates
# and displays the amount of money you’ll have each year at the ends of years 1 through 30.
print("Deposit\t\tNumber_of_years\t\tAmount_on_deposit")
principal = 1000
rate = 7*0.01
for number_of_years in range(1,31):
    amount_on_deposit = principal * ((1 + rate)**number_of_years)
    print(f'{principal:<7}{number_of_years:>15}{amount_on_deposit:>29.2f}')