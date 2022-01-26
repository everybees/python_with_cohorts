pi = 0
term = int(input('Enter the number of terms to be approximated'))
for n in range(term):
    n +=2
    pi += 4-(4/n)+(4/n+2)-(4/n+4)+(4/n+6)-(4/n+8)
print(pi)