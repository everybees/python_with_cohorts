# Author : Joshua

count = 0
onewins = 0
twowins = 0

while count < 10:
    count += 1

    if int(input('Type First Number: ')) == int(input('Type Second Number: ')):
        print('Second player wins')
        twowins += 1
    else:
        print('First player wins')
        onewins += 1

print('First player got: ', onewins, '\nSecond player got: ', twowins,)
if onewins > twowins:
    print('Player One is the winner')
else:
    print('Player Two is the winner')
