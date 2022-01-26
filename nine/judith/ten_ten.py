def ten_ten_method():
    player_one_score = 0
    player_two_score = 0
    for i in range(5):
        leg_one = input('Enter a value:')
        leg_two = input('Enter a  value:')

        if leg_one == leg_two:
            print('the winner is leg two')
            player_two_score += 1

        elif leg_one != leg_two:
            print('the winner is leg one')
            player_one_score += 1

    print('Leg one scored', player_one_score)
    print('Leg two scored', player_two_score)
