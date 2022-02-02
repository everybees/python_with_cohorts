rock = 'rock'
paper = 'paper'
scissors = 'scissors'

user_one_score = 0
user_two_score = 0
draw_score = 0

for i in range(10):
    user_one = input('pick rock,paper or scissors:')
    user_two = input('pick rock,paper or scissors:')

    if user_one == rock and user_two == paper or user_one == paper and user_two == scissors \
            or user_one == scissors and user_two == rock:
        print('user_two wins')
        user_two_score += 1

    elif user_one == user_two:
        print('This is a draw')
        draw_score += 1

    else:
        print('user_one Wins')
    user_one_score += 1

print(user_one_score)
print(user_two_score)
print(draw_score)
