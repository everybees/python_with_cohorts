user_1 = str(input("Ready, Player 1? Rock, Paper, Scissors?: "))
user_2 = str(input("Ready, Player 2? Rock, Paper, Scissors?: "))

if user_1 == "Rock" and user_2 == "Scissors":
    print("Player 1 Wins")
elif user_1 == "Scissors" and user_2 == "Paper":
    print("Player 1 Wins")
elif user_1 == "Paper" and user_2 == "Rock":
    print("Player 1 Wins")

elif user_1 == user_2:
    print("Stalemate, Go Again")
    user_1 = str(input("Ready, Player 1? Rock, Paper, Scissors?: "))
    user_2 = str(input("Ready, Player 2? Rock, Paper, Scissors?: "))

else:
    print("Player 2 Wins")
