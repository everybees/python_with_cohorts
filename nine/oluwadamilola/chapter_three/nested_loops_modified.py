for row in range (1, 11):
    for column in range (0, row):
        print('*', end=" ")
    # print()
    for column in range (11, row, -1):
        print(' ', end=" ")
    # print()
    for column in range (11, row, -1):
        print ('*', end=" ")
    # print()
    for column in range (0, row):
        print(' ',end=" ")
    # print()
    for column in range (0, row):
        print (' ', end=" ")
    # print()
    for column in range (11, row, -1):
        print ('*', end=" ")
    # print()
    for column in range (11, row, -1):
        print (' ', end=" ")
    # print()
    for column in range (0, row):
        print ('*', end=" ")
    print()
