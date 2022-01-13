rock = "r"
paper = "p"
scissors = "s"

player_1_score = 0
player_2_score = 0

for i in range(10):
    player_1_input = input("Enter rock paper or scissors: ")
    player_2_input = input("Enter rock paper or scissors: ")

    if player_1_input == paper and player_2_input == rock:
        player_1_score += 1
    elif player_1_input == scissors and player_2_input == paper:
        player_1_score += 1
    elif player_1_input == rock and player_2_input == scissors:
        player_1_score += 1
    else:
        player_2_score += 1

print(player_1_score)
print(player_2_score)

if player_1_score > player_2_score:
    print("Player One Wins")
elif player_1_score < player_2_score:
    print("Player Two Wins")
