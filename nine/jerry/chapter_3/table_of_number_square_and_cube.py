import math

x = 'number'
counter = 1
while counter < 6:
    if counter == 1:
        print(f' {x:.3s}')
    print(f' {counter:3d}', end="\t\t")
    print(f' {int(math.pow(counter, 2)):3d}', end="\t\t")
    print(f' {int(math.pow(counter, 3)):3d}', end=" ")
    print("\n")
    counter += 1