
user_one_score = 0
user_two_score = 0
for i in range(10):
    user_one_input = input("Enter Rock Paper Or Scissors")
    user_two_input = input("Enter Rock Paper Or Scissors")

    if user_two_input == "rock" and user_one_input == "paper":
        print("Player One Wins")
        user_one_score += 1

    elif user_two_input == "paper" and user_one_input == "scissors":
        print("Player One Wins")
        user_one_score += 1
    elif user_two_input == "scissors" and user_one_input == "rock":
        print("Player One Wins")
        user_one_score += 1
    elif user_two_input == user_one_input:
        print("Draw")

    else:
        print("Player Two Wins")
        user_two_score += 1
print("User One Score : ", user_one_score)
print("User Two Score: ", user_two_score)

if user_two_score > user_one_score:
        print("User  Two Is The Winner !!!!")
elif user_two_score == user_one_score:
    print("Stalemate")
else:
     print("User One is the winner!!!!!")


