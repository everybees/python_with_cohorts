Player1Score = 0
Player2Score = 0

for i in range(10):
    user_1 = str(input("Ready, Player 1? Rock, Paper, Scissors?: "))
    user_2 = str(input("Ready, Player 2? Rock, Paper, Scissors?: "))

    if user_1 == "Rock" and user_2 == "Scissors":
        Player1Score += 1
    elif user_1 == "Scissors" and user_2 == "Paper":
        Player1Score += 1
    elif user_1 == "Paper" and user_2 == "Rock":
        Player1Score += 1

    else:
        Player2Score += 1

print("Player 1 Score: ", Player1Score)
print("Player 2 Score: ", Player2Score)
