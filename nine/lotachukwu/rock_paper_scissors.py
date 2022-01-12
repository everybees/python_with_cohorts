rock = "r"
paper = "p"
scissors = "s"
count = 0
user1_point = 0
user2_point = 0
while count < 10:
    user_input1 = input("enter rock,paper,scissors: ")
    user_input2 = input("enter rock,paper,scissors: ")
    if user_input1 == rock and user_input2 == scissors:
        print("user 1 wins")
        user1_point += 1
    if user_input1 == scissors and user_input2 == rock:
        print("user 2 wins")
        user2_point += 1
    if user_input2 == paper and user_input1 == scissors:
        print("user 1 wins")
        user1_point += 1
    if user_input2 == scissors and user_input1 == paper:
        print("user 2 wins")
        user2_point += 1
    if user_input1 == rock and user_input2 == paper:
        print("user 2 wins")
        user2_point += 1
    if user_input1 == paper and user_input2 == rock:
        print("user 1 wins")
        user1_point += 1
    if user_input2 == user_input1:
        print("equal")
    count += 1
    print(user1_point)
    print(user2_point)
    if user1_point > user2_point:
        print("user 1  is winner")
if user2_point > user1_point:
    print("user 2 is  winner")
