a = b = 7
print('a =', a, 'i =', b)

for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
        print()
