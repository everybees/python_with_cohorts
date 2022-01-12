left_leg = 1
right_leg = 2

print("instructions: Enter 1 for left leg, Enter 2 for right leg")

player1 = int(input("Player1: Enter a number: "))
player2 = int(input("Player2: Enter a number: "))

if player1 == left_leg and player2 == right_leg: print("Player 1 wins")
elif player1 == left_leg and player2 == left_leg: print("Player 2 wins")
elif player1 == right_leg and player2 == left_leg: print("Player 1 wins")
elif player1 == right_leg and player2 == right_leg: print("player 2 wins")
elif player1 != left_leg or right_leg and player2 != left_leg or right_leg: print("Please read game instructions")
