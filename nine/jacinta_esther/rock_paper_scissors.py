rock = "r"
paper = "p"
scissors = "s"

count = 1
player1_point = 0
player2_point = 0
draw = 0
while count < 11:
    count = count + 1
    player_1 = input("Enter a letter between r, p and s for player 1: ")
    player_2 = input("Enter a letter between r, p and s for player 2: ")
    print()
    if player_1 == rock and player_2 == scissors or player_1 == paper and player_2 == rock \
            or player_1 == scissors and player_2 == paper:
        player1_point += 1
    elif player_1 == player_2:
        draw += 1

    else:
        player2_point += 1

print("player 1 point is: ", player1_point)
print("player 2 point is: ", player2_point)
print("draw value is: ", draw)
if player1_point > player2_point:
    print("player1 wins")
elif player1_point == player2_point:
    print("draw")
else:
    print("player2 wins")
