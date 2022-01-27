passes = 0
failures = 0

while passes + failures != 10:
    result = int (input("Enter result (1 = pass, 2 = fail): "))
    if result == 1:
        passes += 1
    if result == 2:
        failures+= 1

print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')