
player_one_score = 0
player_two_score = 0

for i in range(10):
    player_one_pick = input("Enter Rock Paper Or Scissors")
    player_two_pick = input("Enter Rock Paper Or Scissors")

    if player_two_pick == "rock" and player_one_pick == "paper":
        print("Player One Wins")
        player_one_score += 1

    elif player_two_pick == "paper" and player_one_pick == "scissors":
        print("Player One Wins")
        player_one_score += 1
    elif player_two_pick == "scissors" and player_one_pick == "rock":
        print("Player One Wins")
        player_one_score += 1
    elif player_two_pick == player_one_pick:
        print("Draw")

    else:
        print("Player Two Wins")
        player_two_score += 1
print("User One Score : ", player_one_score)
print("User Two Score: ", player_two_score)

if player_two_score > player_one_score:
    print("User  Two Is The Winner !!!!")
elif player_two_score == player_one_score:
    print("Stalemate")
else:
    print("User One is the winner!!!!!")


