first_total = 0
second_total = 0
for i in range(5):
    first_player = input('enter left or right')
    second_player = input('enter left or right')
    if first_player == second_player:
        print("second player wins")
        second_total += 1
    else:
        print('first player wins')
        first_total += 1

        print("first_player scores:", first_total, "second player scores:", second_total)
