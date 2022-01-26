import math

print(' number\tsquare\tcube')
for i in range(6):
    print(f'{i:>6} {i**2:>6}  {i**3:>6}')

i = 2
power = math.pow(i, 2)
print(power)
