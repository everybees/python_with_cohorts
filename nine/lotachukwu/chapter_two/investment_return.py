print('Initial amount   year       Interest accumulated')
p = 1000
r = 0.07
year = 10

for i in range(year, 40, 10):
    simple_interest = p * (1 + r) ** i
    print(p, "\t\t\t", i, "\t\t", simple_interest)
