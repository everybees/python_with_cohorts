import math

print('number\t square\t cube')
for i in range(6):
    print(f'{i:>6} {int(math.pow(i,2)):>6} {int(math.pow(i,3)):>6}')
