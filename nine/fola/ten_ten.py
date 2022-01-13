
ade = 0
bayo = 0
leg_1 = "l"
leg_2 = "r"

for i in range(10):
    ade_1 = input("Put a foot forward: ")
    bayo_1 = input("Put a foot forward: ")
    if ade_1 == "l" and bayo_1 == "r":
        ade += 1
        print("Ade Wins!!!")
    elif ade_1 == "r" and bayo_1 == "l":
        print("player 1 Wins!!!")
        ade += 1
    elif ade_1 == bayo_1:
        print("Bayo Wins!!!")
        bayo += 1
print("Ade wins", ade, "time", "while", "Bayo wins", bayo, "times")




