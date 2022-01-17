
passes = 0

failures = 0
count = 0

for i in range(10):

    result = int(input("Enter result(1 = Pass, 2 =Fail): "))
    if result != 1 or result != 2:
        if result == 1:
            passes = passes + 1
        else:
            failures = failures + 1

print('Passed: ', passes)
print(' Failed: ', failures)

if passes > 8:
    print('Bonus to the instructor')

