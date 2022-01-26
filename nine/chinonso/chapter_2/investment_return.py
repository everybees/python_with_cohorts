p = int(input('Enter amount to be invested:'))
n = int(input('Enter the years of investment:'))
r = 7/100
a = p*((1 + r)**n)
print('The amount on deposit at',n,'th year is',a)