for i in range(1,11):
    for j in range(0,i):
        print('*',end='')
    for j in range(0,11-i-1):
        print(' ', end='')
    for j in range(0,11-i):
        print('*',end='')
    for j in range(0,2*i):
       print(' ',end='')
    for j in range(0,11-i):
       print('*',end='')
    for j in range(0,11-i-1):
        print(' ',end='')
    for j in range(0,i):
        print('*',end='')
        print()  