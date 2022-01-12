player_one_point =0;
player_two_point =0;
count =0;
while(count < 3):
    user_input_1 =input("Enter rock, paper or scissors: ")
    user_input_2 = input("Enter rock, paper or scissors: ")

    if user_input_1 == "rock" and user_input_2 == "paper" or user_input_1 == "scissors" and user_input_2 == "rock" or user_input_1 == "paper" and user_input_2 == "scissors":
        print("user two wins")
        player_two_point +=1
    elif user_input_1 == "rock" and user_input_2 == "scissors" or user_input_1 == "rock" and user_input_2 == "paper" or user_input_1 == "scissors" and user_input_2 == "paper":
        print("user one wins")
        player_one_point +=1
    else:
        print("Stalemate")
    count+=1

if player_one_point > player_two_point:
    print("Player one wins with ", player_one_point, "points")
elif player_one_point < player_two_point:
    print("Player two wins with ", player_two_point, "points")
else:
    print("Draw")