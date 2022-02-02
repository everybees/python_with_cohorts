def ten_ten():
    user1=0
    user2=0

    left = "l"
    right = "r"

    for i in range (10):
        user_input1=input("Enter l for left or r for right: ")
        user_input2=input("Enter l for left or r for right: ")

        if(user_input1==left and user_input2== right):
            print("user1 wins!")
            user1+=1

        if(user_input1==right and user_input2==left):
                print("user2 wins!")
                user2+=1

        if(user_input1==user_input2):
            print("It's a draw") 

    print("The scores for user1 is: ", user1)   
    print("The scores for user2 is: ", user2)

    if(user1 > user2):
            print("The winner is user1 with the highest score of: ", user1)
    elif(user2 >user1):
            print("THe winner is user2 with the highest score of: ",user2) 


def tired_class():
    print("We are tired!!!")
    print("Let us go on break!!!")