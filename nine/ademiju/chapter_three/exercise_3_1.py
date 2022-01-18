pass_counter = 0
fail_counter = 0
score = int(input('Enter 1 for pass or 2 for fail or enter 3 to exit '))
while(score != 3):
    if(score == 1):
        pass_counter += 1
    else:
        fail_counter += 1
    score = int(input('Enter 1 for pass or 2 for fail or enter 3 to exit '))
print('You entered',fail_counter,'fail(s)')


