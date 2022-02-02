p = int(input('Enter amount to be invested:'))
for n in range(30):
    r = 7/100
    a = p*((1 + r)**n)
    print('The amount on deposit at year',n, 'is',f'{a:.3f}')