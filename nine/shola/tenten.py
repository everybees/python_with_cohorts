
first_total = 0
second_total = 0

for i in range(10):
    first_player = input("left or right")
    second_player = input("left or right")

    if first_player == second_player:
        print('second player wins')
        second_total += 1
    else:
        print('first player wins')
        first_total += 1

print("First Player scores: ", first_total, "Second player scores: ", second_total)
if first_total > second_total:
    print("First player is the Winner")
else:
    print("Second player is the Winner")

