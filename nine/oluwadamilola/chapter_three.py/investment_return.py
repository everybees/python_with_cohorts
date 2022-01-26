print('Years      Principal      Investment Return')
for year in range (31):
    print(f'{year:<6}{1000:>10}{(1000*(1 + 0.07)**year):>20.2f}')
