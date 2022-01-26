# Author: Joshua
# Title : Validating User Input 3.1


passes = 0
failures = 0
result = 1
# process 10 students
while result == 1 or result == 2:
    counter = +1
    result = int(input('Enter result (1=pass,2=fail): '))

    if result == 1:
        passes = passes + 1
    else:
        failures = failures + 1

    print('Passed:', passes)
    print('Failed:', failures)

    if passes > 8:
        print('Bonus to instructor')
