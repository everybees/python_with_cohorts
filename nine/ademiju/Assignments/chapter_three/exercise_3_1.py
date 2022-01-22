pass_counter = 0
fail_counter = 0
total_score_counter = 0
score = int(input('Enter 1 for pass or 2 for fail or enter 0 to exit '))
while(score < 0 or score > 2):
    score = int(input('Invalid Input!!!Enter 1 for pass or 2 for fail or enter 0 to exit '))

while(score !=0 ):
    if(score == 1):
        pass_counter += 1
        total_score_counter +=1
    else:
     fail_counter += 1
     total_score_counter +=1
     score = int(input('Enter 1 for pass or 2 for fail or enter 0 to exit '))

if total_score_counter > 0:
    print('You entered',fail_counter,'fail(s)')
    print('You entered',pass_counter,'fail(s)')
else:
    print('No score entered, restart program to enter score')



