user_one_score = 0
user_two_score = 0
for i in range(10):
    user_one_input = input("Enter Rock Paper Or Scissors")
    user_two_input = input("Enter Rock Paper Or Scissors")

    draw = user_two_input == user_one_input
    user_one_wins = user_two_input == "rock" and user_one_input == "paper" or user_two_input == "paper" and user_one_input == "scissors" or user_two_input == "scissors" and user_one_input == "rock"

    if user_one_wins:
        print("Player One Wins")
        user_one_score += 1

    elif draw:
        print("Draw")

    else:
        print("Player Two Wins")
        user_two_score += 1
print("User One Score : ", user_one_score)
print("User Two Score: ", user_two_score)

user_two_wins = user_two_score > user_one_score
stalemate = user_two_score == user_one_score
if user_two_wins:
    print("User  Two Is The Winner !!!!")
elif stalemate:
    print("Stalemate")
else:
    print("User One is the winner!!!!!")
