count1 = 0
count2 = 0
for i in range(2):
    player1 = input('first player: Enter your choice, right and left :')
    player2 = input('second player: Enter your choice, right and left :')
    if player1 == player2:
        count2 +=1
    if player1 != player2:
        count1 += 1

print("Player 1 has ",count1,"point")
print("Player 2 has ",count2,"point")