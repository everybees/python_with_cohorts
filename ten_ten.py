scoreCounter=0
rightLeg="rl"
leftLeg="ll"
player1Counter=0
player2Counter=0

while scoreCounter<=5:

    player1=input("enter left or right leg")
    player2=input("enter left or right leg")
    scoreCounter = scoreCounter + 1
    if(player1==rightLeg and player2==leftLeg):player1Counter=player1Counter+1
    if(player2==rightLeg and player1==leftLeg):player1Counter=player1Counter+1
    if(player1==leftLeg and player2==rightLeg):player1Counter=player1Counter+1
    if(player2==leftLeg and player1==rightLeg):player2Counter=player2Counter+1
    if(player1==rightLeg and player2==rightLeg):player2Counter=player2Counter+1
    if(player2==rightLeg and player1==rightLeg):player1Counter=player1Counter+1
    if(player1==leftLeg and player2==leftLeg):player2Counter=player2Counter+1
    if(player2==leftLeg and player1==leftLeg):player1Counter=player1Counter+1

    print(player1Counter, player2Counter)

