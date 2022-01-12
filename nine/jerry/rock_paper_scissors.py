rock = 'r'
paper = 'p'
scissors = 's'
print('Enter one of the following characters: r, p, s')
user_one = 0
user_two = 0
stalemate = 0
counter = 0
# while counter < 5:
for i in range(5):
    user1 = input('r, p or s? ')
    user2 = input('r, p or s? ')
    if user1 == paper and user2 == rock:
        print('User1 wins!')
        user_one += 1
    elif user1 == rock and user2 == scissors:
        print('User1 wins!')
        user_one += 1
    elif user1 == scissors and user2 == paper:
        print('User1 wins!')
        user_one += 1
    elif user1 == user2:
        print('Stalemate')
        stalemate += 1
    else:
        print('User2 wins')
        user_two += 1
    # counter += 1
print('User1 wins ', user_one, ':', 'User2 wins ', user_two)
print(stalemate, 'Stalemate')
