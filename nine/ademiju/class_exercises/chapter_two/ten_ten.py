player_one_score = 0
player_two_score = 0
draw = 0
left = "l"
right = "r"

for count in range (10):
    player_one_input = input("Enter r for right leg or l for left leg ")
    player_two_input = input("Enter r for right leg or l for left leg ")

    if(player_one_input == left and player_two_input == left):
         print("Player Two Wins this round")
         player_two_score+=1 
    if(player_one_input == left and player_two_input == right):
            print("Player One Wins this round") 
            player_one_score+=1
    if (player_one_input == right and player_two_input == right):
        print("Player Two Wins this round")
        player_two_score+=1
    if(player_one_input == right and player_two_input == left):
        print("Player One Wins")
        player_one_score+=1

print("Player one score = \n",player_one_score,"Playere two score =",player_two_score)

if(player_one_score > player_two_score):
    print("Player One Wins the Game")
elif(player_two_score > player_one_score):
    print("Player Two Wins the Game")

else:print("Its a DRAW")


      


