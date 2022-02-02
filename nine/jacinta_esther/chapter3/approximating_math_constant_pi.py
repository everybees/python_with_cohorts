pi = 0
numerator = 4
denominator = 1
for i in range(200_000):
    if i % 2 == 1:
        pi += -(numerator / denominator)
    else:
        pi += (numerator / denominator)
    denominator += 2
    print("Pi is ", pi)

print("Final value of pi is ", pi)
