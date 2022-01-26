left_leg = 'll'
right_leg = 'rl'

player_one_score =0
player_two_score = 0


for i in range(2):
    player1_leg = input("Player1, enter a leg: ")
    player2_leg = input("Player2, enter a leg: ")

    if(player2_leg == player1_leg):
        player_two_score += 1
    elif(player1_leg == player2_leg):
        player_one_score += 1
if(player_two_score > player_one_score):
    print("Player two wins with", player_two_score)
if(player_one_score > player_two_score):
    print("Player one wins with", player_one_score)
    