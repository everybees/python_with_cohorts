principal = 1000
rate = 0.07
years = 10

for i in range(years, 40, 10):
    simple_interest = principal * (1 + rate) ** i

    print(simple_interest)