player1score = 0
player2score = 0

for i in range(10):
    right = 'right'
    left = 'left'
    player1 = input("Enter right,left:")
    player2 = input("Enter right,left:")

    if player1 == right and player2 == right:
        print('player2 Wins')
        player2score += 1

    elif player1 == right and player2 == left:
        print('player1 Wins')
        player1score += 1

    elif player1 == left and player2 == right:
        print('player1 Wins')
        player1score += 1

    elif player1 == left and player2 == left:
        print('player2 Wins')
        player2score += 1

print('player1score', player1score)
print('player2score', player2score)
