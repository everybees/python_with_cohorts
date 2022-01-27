
passes = 0
failures = 0

for student in range(3):
    result = int(input('Enter result (1=pass, 2=fail): '))
    if result == 1:
        passes = passes + 1
    elif result == 2:
        failures = failures + 1
while result != 1 or result != 2:
        result = int(input('Enter result (1=pass, 2=fail): '))

print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
              print('Bonus to instructor')