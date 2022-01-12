
count = 1
player1_point = 0
player2_point = 0
draw = 0

while count < 11 :
    count = count + 1
    player_1 = input("Enter a number: ")
    player_2 = input("Guess the number entered by player 1: ")
    print()
    if player_1 == player_2:
        player2_point +=1
    else :
        player1_point += 1

print("player 1 point is: ", player1_point)
print("player 2 point is: ", player2_point)
if player1_point > player2_point:
    print("player1 wins")
else:
    print("player2 wins")
