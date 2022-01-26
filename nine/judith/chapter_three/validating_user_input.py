passes = 0
failures = 0
for student in range(10):
    result = int(input('Enter result(1 = pass, 2 = fail):'))
    if result == 1:
        passes = passes + 1

    elif result == 2:
        failures = failures + 1
    else:
        print(result, 'is a wrong input:')

print('Passed:', passes)
print('Failed:', failures)
