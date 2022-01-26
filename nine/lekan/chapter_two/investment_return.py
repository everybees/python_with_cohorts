amount_invested = 1000
investment_return = 0.07
years = 0
amount_on_deposited = 0

for i in range(3):
    years += 10
    amount_on_deposit = amount_invested*(1 + investment_return)**years
    print("In ", years, "years the amount on investment is ", amount_on_deposit)

