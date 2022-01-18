for i in range(20):
    for j in range(20):
        for k in range(20):
            pythagorean_triples = (i * i) + (j * j) == k * k
            if pythagorean_triples:
                print(i, j, k)

print()
