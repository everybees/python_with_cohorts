rock = "r"
paper = "p"
scissors = "s"

player_1_score = 0
player_2_score = 0

player_1_input = input("Enter rock paper or scissors: ")
player_2_input = input("Enter rock paper or scissors: ")

if player_1_input == paper and player_2_input == rock:
    print("User One Wins!")
if player_1_input == scissors and player_2_input == paper:
    print("User One Wins!")
if player_1_input == rock and player_2_input == scissors:
    print("User One Wins!")
else:
    print("Player Two Wins")
