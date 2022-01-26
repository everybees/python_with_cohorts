rock = 'r'
paper = 'p'
scissors = 's'
first_user_score = 0
second_user_score = 0

for i in range(10):

    first_user = str(input("Enter one of the following 'r' 'p' 's'"))
    second_user = str(input("Enter one of the following 'r' 'p' 's"))
    if first_user == 'p' and second_user == 'r':
        print("first_user wins")
        first_user_score += 1
    elif first_user == 's' and second_user == 'p':
        print("first_user wins")
        first_user_score += 1
    elif first_user == 'r' and second_user == 's':
        print("first_user wins")
        first_user_score += 1
    elif first_user == second_user:
        print("draw")
    else:
        print("user_two wins")
        second_user_score += 1

print("user one wins", first_user_score, "user two wins", second_user_score)
