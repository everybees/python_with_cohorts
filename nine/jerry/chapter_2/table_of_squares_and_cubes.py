import math

print("number\tsquare\tcube")
counter = 1
while counter < 6:
    print(counter, end="\t\t")
    print(int(math.pow(counter, 2)), end="\t\t")
    print(int(math.pow(counter, 3)), end=" ")
    print("\n")
    counter += 1