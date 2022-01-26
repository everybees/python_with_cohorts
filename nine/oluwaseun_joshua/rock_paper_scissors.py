rock="rock"
scissor="sccissor"
paper="paper"

# user1=input("enter a rock,sccissor or paper:  ")
# user2=input("enter a rock or sccissor or paper:   ")



player1_score=0
player2_score=0

for i in range(10):
    user1=input("enter a rock,sccissor or paper:  ")
    user2=input("enter a rock or sccissor or paper:   ")

    if(user1=="rock" and user2== "scissor"):
      print("player1 wins")
      player1_score += 1

    if(user1=="scissor" and user2=="rock"):
      print("player2 wins")
      player2_score += 1

    if(user1=="paper" and user2=="rock"):
       print("player1 wins")
    player1_score += 1
    if(user1=="rock" and user2=="paper"):
       print("player2 wins")
    player2_score += 1
    if (user1=="scissor" and user2=="paper"):
       print("player1 wins")
    player1_score += 1
    if(user1=="paper" and user2=="scissor"):
       print("player2 wins")
    player2_score += 1


    # elif(user1==user2):
    #    print("stalemen")



if(player1_score > player2_score):
    print("player1 won with total value of",player1_score)

elif(player1_score < player2_score):
    print("player2 won with total value of ",player2_score)

elif(player1_score==player2_score):
    print("It's a draw")