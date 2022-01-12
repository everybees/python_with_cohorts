import math

# radius = input("Enter a number")
# radius_convert = int(radius)

# circum = 2 * math.pi * radius_convert
# print(circum)

# area = math.pi * radius_convert ** 2
# print(area)


#Rock Paper Scissors
rock = "rock"
paper = "paper"
scissors = "scissors"

player1_score = 0
player2_score = 0

for i in range(10):
    user1 = input("Player1: Enter rock, paper or scissors: ")
    user2 = input("Player2: Enter rock, paper, or scissors: ")

    if user1 == "rock" and user2 == "paper":
        print("Result = Player2: paper wins")
        player2_score += 1
    elif user1 == "paper" and user2 == "rock":
        print("Result = Player1: paper wins")
        player1_score += 1
        
    elif user1 == "rock" and user2 == "scissors":
        print("Result = Player1: rock wins")
        player1_score += 1
    elif user1 == "scissors" and user2 == "rock":
        print("Result = Player2: rock wins")
        player2_score += 1

    elif user1 == "scissors" and user2 == "paper":
        print("Result = Player1: scissors wins")
        player1_score += 1
    elif user1 == "paper" and user2 == "scissors":
        print("Result = Player2: scissors wins")
        player2_score += 1
    

print("Player1 score = ", player1_score)
print("Player2 score = ", player2_score)

        
    





#Ten roounds, two players, output their score.