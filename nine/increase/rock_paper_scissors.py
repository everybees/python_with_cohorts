rock = "r"
paper = "p"
scissors = "s"

user1=0
user2=0

for i in range(10):
    user_input_1 = input("Enter either r for rock, p for paper, s for scissors: ")
    user_input_2 = input("Enter either r for rock, p for paper, s for scissors:")


    if(user_input_1 == rock and user_input_2 == paper):
        print("user1 wins!")
        user1+=1

    if(user_input_1==rock and user_input_2== scissors):
        print("user1 wins!")
        user1+=1

    if(user_input_1==paper and user_input_2==rock):
        print("user1! wins!")
        user1+=1

    if(user_input_1== paper and user_input_2==scissors):
        print("user2 wins!")
        user2+=1

    if(user_input_1== scissors and user_input_2== paper):
        print("user1 wins!") 
        user1+=1

    if(user_input_1== scissors and user_input_2==rock):
        print("user2 wins!")
        user2+=1

    if(user_input_1==user_input_2):
        print("This is a draw")

print("The total score for user1 is: ",user1)
print("The total score for user2 is: ",user2)

if(user1 > user2):
    print("The winner is user1 with the highest score of: ",user1)
elif(user2 > user1):
    print("The winner is user2 with the highest score of: ",user2)