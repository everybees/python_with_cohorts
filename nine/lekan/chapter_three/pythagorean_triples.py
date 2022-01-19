for i in range(21):
    for j in range(21):
        for k in range(21):
            pythagorean_triples = (i * i) + (j * j) == k * k
            if pythagorean_triples:
                print(i, j, k)

print()
