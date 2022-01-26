
for i in range(1, 7):
    for a in range(1, i):
        print(a, end=" ")
    print("\n")

count = 6
while count >= 1:
    for k in range(1, count+1):
        if count < 6:
            print(count - (k - 1), end=" ")
    print("\n")
    count -= 1
