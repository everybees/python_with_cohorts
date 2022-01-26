print("Hypotenuse\tSide1\tSide2")
for i in range(500):
    for j in range(i):
        for k in range(j):
            a = j ** 2 + k ** 2
            if a == (i ** 2): print(i, "^2\t\t", j, "^2\t", k, "^2")
