left_leg = "l"
right_leg = "r"

first_player_count = 0
second_player_count = 0

for i in range(10):
    first_player = input("Enter r for right leg and l for left leg:  ")
    second_player = input("Enter r for right leg and l for left leg:  ")

    if first_player == "r" and second_player =="r" or first_player == "l" and second_player == "l":
        print("Second player wins!!")
        second_player_count += 1

    if first_player == "r" and second_player == "l" or first_player == "l" and second_player == "r":
            print("First player wins!!")
            first_player_count += 1
print("First player has ", first_player_count, "point(s)", "\nSeconD player has ", second_player_count, "point(s)")

if first_player_count > second_player_count:
    print("First player wins!!")
elif second_player_count > first_player_count:
    print("Second player wins!!")
else: 
    print("It is a draw.")

