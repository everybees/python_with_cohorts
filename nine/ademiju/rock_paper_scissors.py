first_player_score = 0
second_player_score = 0
draw = 0
for count in range(10):
 first_player_input = input("Enter 'R' for rock, 'P' for paper or 'S' for scissors ")
 second_player_input = input("Enter 'R' for rock, 'P' for paper or 'S' for scissors ")
 rock = 'r'
 paper = 'p'
 scissors = 's' 

 if(first_player_input == rock and second_player_input == paper ):
      print("Second player Wins this round")
      second_player_score+=1
 if(first_player_input == rock and second_player_input == scissors):
          print("First Player Wins this round")
          first_player_score+=1
                   
 if(first_player_input == paper and second_player_input == scissors ):
      print("Second player Wins this round")
      second_player_score+=1
 if(first_player_input == paper and second_player_input == rock):
          print("First Player Wins this round")
          first_player_score+=1
    
 if(first_player_input == scissors and second_player_input == paper ):
      print("First player Wins this round")
      first_player_score+=1
 if(first_player_input == scissors and second_player_input == rock):
          print("Second Player Wins this round")
          second_player_score+=1
          
 if(first_player_input == second_player_input):
            print("This round is a Draw ")
            draw+=1

print("player One Score = ",first_player_score)
print("Player Two score = ",second_player_score)
print("Draw = ",draw)

if(first_player_score > second_player_score):
    print("Player One Wins the game")

if(second_player_score > first_player_score):
    print("Second Player Wins the game")

if(first_player_score == second_player_score):
    print("The game is a Draw")
