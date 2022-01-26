def ten_ten():
    right_leg = "rl"
    left_leg = "ll"

    player_1_score = 0
    player_2_score = 0

    for i in range(10):
        player_1_input = input("Enter your first leg value here: ")
        player_2_input = input("Enter your second leg value here: ")

        if player_1_input == "rl" and player_2_input == "ll":
             player_1_score += 1

        elif player_1_input == "ll" and player_2_input == "rl":
             player_2_score += 1

        elif player_1_input == player_2_input:
             player_1_score += 1
             player_2_score += 1

    print(player_1_score)
    print(player_2_score)

    if player_1_score > player_2_score:
        print("Player One Wins")
    elif player_1_score < player_2_score:
        print("Player Two Wins")

