rock='r'
paper='p'
scissors='s'
user1=input("Enter a choice r, p, s:  ")
user2=input("Enter a choice r, p, s: ")
player1=user1
player2=user2

if user1 == "r" and user2 =="p":
  print("player1 wins")

if user2 =="r" and user1 =="p":
    print("player2 wins")


if user1 == "s" and user2 =="p":
    print("player1 wins") 
if user2 == "s" and user1 =="p":
    print("player2 wins")

if user1 == "r" and user2 =="s":
    print("player1 wins")   
if user2 == "r" and user1 =="s":
    print("player2 wins")

if user1 == user2:
    print("draws")