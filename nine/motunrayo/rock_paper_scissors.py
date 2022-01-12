user1_point =0
user2_point =0
for i in range(10):
    user_1 = input("Enter rock,paper,scissors:")
    user_2 = input("Enter rock,paper,scissors:")
    
    if(user_1 == "paper" and user_2 == "scissors"):
        print("user two wins")
        user2_point+=1
    elif(user_1 == "scissors" and user_2 == "rock"):
        print("user two wins")
        user2_point+=1
    elif(user_1 == "rock" and user_2 == "scissors") :
        print ("user one wins") 
        user1_point+=1  
    elif(user_1 == "rock" and user_2 == "paper"):
        print ("user two wins")
        user2_point+=1
    elif(user_1 == "scissors" and user_2 == "paper"):
        print("user one wins")
        user1_point+=1
    elif(user_1 == "paper" and user_2 == "scissors"):
        print("user two wins")
        user2_point+=1
    elif(user_1 == "rock" and user_2 == "rock"):
        print("whoop!!! no one wins")                               
print("player 1 point is: ", user1_point) 
print("player 2 point is: ", user2_point) 
if user1_point > user2_point:
    print("user one wins")
elif user2_point > user1_point:
    print("user two wins")  
else:
    print("it is a tie")                   
                            


