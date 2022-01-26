user_input = int(input("Enter a number:  "))
numerator = 1
result = 0
total2 = 0
for i in range(1, user_input):
    total = 1
    for j in range(1, i):
        total *= j

    result = numerator / total
    total2 += result

print(1 + total2)

