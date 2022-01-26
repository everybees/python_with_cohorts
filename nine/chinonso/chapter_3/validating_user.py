passes = 0
failure = 0
while (passes + failure) != 10:
    result = int(input('Enter result; 1 or 2 :'))
    if result == 1:
        passes = passes + 1
    if result == 2:
        failure = failure + 1

print('passes:',passes)
print('failure :',failure)

