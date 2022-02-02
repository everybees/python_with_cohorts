# Author : Joshua
count = 0
onewins = 0
twowins = 0
draws = 0 
while count < 10:
    count += 1
    one = input("input Rock or paper or scissors")
    two = input('input Rock or paper or scissors')

    if one == 'rock' and two == 'scissors' or one == 'paper' and two == 'rock' or one == 'scissors' and two == 'paper':
        print('One Wins')
        onewins += 1

    elif one == two:
        print('No winner')
        draws += 1
    else:
        print('Two Wins')
        twowins += 1
        
print('First player got: ', onewins, '\nSecond player got: ', twowins, '\nThe draws were: ', draws)
if onewins > twowins:
    print('Player One is the winner')
else:
    print('Player Two is the winner')