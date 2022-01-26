print("Initial amount\t\t\tyear\t\t\tInterest accumulated")
p = 1000
r = 0.07
year = 10

for i in range(1, 30):
    simple_interest = p * (1 + r) ** i
    print(f'{p:> 13}  {i :> 12} {simple_interest:>31.2f}')



