pass_counter = 0
fail_counter = 0
score = int(input('Enter 1 for pass or 2 for fail '))
for result in range(10):
    while(score < 0 or score > 2):
        score = int(input('Invalid Input!!!Enter 1 for pass or 2 for fail '))
    if(score == 1):
            pass_counter += 1   
    if(score == 2):
            fail_counter += 1

    score = int(input('Enter 1 for pass or 2 for fail '))


if fail_counter > 0 or pass_counter > 0:
    print('You had',fail_counter,'fail(s)',pass_counter,'pass(es)')
else:
    print('No score entered, restart program to enter score')



