for i in range(10):
    for j in range(i):
        print("*", end=" ")
    for j in range(i, 10):
        print(" ", end=" ")
    for j in range(i, 10):
        print("*", end=" ")
    for j in range(1, i):
        print(" ", end=" ")
    for j in range(1, i):
        print(" ", end=" ")
    for j in range(i, 10):
        print("*", end=" ")
    # for j in range(i, 10):
    #   print("*", end=" ")
    for j in range(i, 10):
        print(" ", end=" ")
    for j in range(1, i):
        print("*", end=" ")
    print()
