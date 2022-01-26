rock='r'
paper='p'
scissors='s'
#=input("Enter a choice r, p, s:)  ")
#user2=input("Enter a choice r, p, s:) ")
#player1=user1
#player2=user2

player1_score=0
player2_score=0
for i in range(10):
    user1=input("Enter a choice r, p, s:  ")
    user2=input("Enter a choice r, p, s: " )

    if user1 == "r" and user2 =="p":
      print("player1 wins")
    player1_score+=1
    if user2 =="r" and user1 =="p":
        print("player2 wins")
    player2_score+=1

    if user1 == "s" and user2 =="p":
        print("player1 wins") 
        player1_score+=1
    if user2 == "s" and user1 =="p":
        print("player2 wins")
        player2_score+=1

    if user1 == "r" and user2 =="s":
        print("player1 wins")
        player1_score+=1   
    if user2 == "r" and user1 =="s":
        print("player2 wins")
        player2_score+=1

   # if user1 == user2:
    #    print("draws")

    if player2_score>player1_score:
        print("player2 wins",player2_score)

    else:
        print("player1 wins",player1_score)