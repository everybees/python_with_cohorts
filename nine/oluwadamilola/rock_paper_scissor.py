rock = "r"
paper = "p"
scissor = "s"

player1_count = 0
player2_count = 0
draw = 0

for i in range(10):
    first_player = input("Enter your choice among r for rock, p for paper and s for scissor: ")
    second_player = input("Enter your choice among r for rock, p for paper and s for scissor: ")
    if first_player == rock and second_player == scissor or first_player == paper and second_player == rock \
        or first_player == scissor and second_player == paper:
        player1_count+=1
        print ("First player wins!!")
       
    elif first_player != second_player: 
        player2_count += 1 
        print ("Second Player wins!!")  

    if first_player == second_player:
            draw+=1
            print("It is a draw!")
      


print ("First player has ", player1_count, "point(s)")
print ("Second player has ", player2_count, "point(s)") 
print ("Both players have a draw of ", draw, "point(s)")

if player1_count > player2_count:
    print ("First Player wins!!")
elif player1_count == player2_count:
    print ("Stalemate")
else:
    print("Second PLayer wins!!")
