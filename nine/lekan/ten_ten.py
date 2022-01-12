player_one_score = 0
player_two_score = 0

for i in range(5):
    play_one = input("Enter a value: ")
    play_two = input("Enter a value: ")

    if play_one == play_two:
        print("winner is leg two")
        player_two_score += 1
    elif play_one != play_two:
        print("Thw winner is leg one")
        player_one_score += 1

print("Leg one score is ", player_one_score)
print("Leg two score is ", player_two_score)
