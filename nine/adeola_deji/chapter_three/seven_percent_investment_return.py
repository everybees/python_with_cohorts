principal = 1000
rate = 0.07
years = 10

print("Year\t\tAmount")
for i in range(30):
    simple_interest = principal * (1 + rate) ** i

    print(f' {i+1:>2} {"":>10} { simple_interest :.2f}')