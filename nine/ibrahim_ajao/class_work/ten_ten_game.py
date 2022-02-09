player_one_point = 0
player_two_point = 0

for i in range(5):
    play_one_leg = input("Enter a value: ")
    play_two_leg = input("Enter a value: ")

    if play_one_leg == play_two_leg:
         print("winner is leg two")
         player_two_point += 1
    elif play_one_leg != play_two_leg:
         print("The winner is leg one")
         player_one_point += 1
    elif play_two_leg == play_one_leg:
         print("Winner is leg one")
         player_one_point += 1
    elif play_two_leg != play_one_leg:
         print("Winner is leg two")
         player_two_point += 1

print("Player one score is ", player_one_point)
print("Player two score is ", player_two_point)
