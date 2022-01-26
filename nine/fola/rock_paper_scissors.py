
rock = "rock"
paper = "paper"
scissors = "scissors"
draw = 0
ade = 0
bayo = 0

for i in range(10):
    player_1 = input("Choose one between rock, paper or scissors: ")
    player_2 = input("Choose one between rock, paper or scissors: ")
    if player_1 == paper and player_2 == rock:
        ade += 1
        print("player 1 Wins!!!")
    elif player_1 == scissors and player_2 == paper:
        print("player 1 Wins!!!")
        ade += 1
    elif player_1 == rock and player_2 == scissors:
        print("player 1 Wins!!!")
        ade += 1
    elif player_1 == player_2:
        print("Nobody Wins - Draw!!!")
        draw +=1
    else:
        print("player 2 Wins!!!")
        bayo += 1

print("Player 1's score is: ", ade, "and Player 2's score is: ", bayo)
print("Number of draw(s) are: ", draw)

