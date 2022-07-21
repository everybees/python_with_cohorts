def ten_ten():
    player_one_score = 0
    player_two_score = 0

    for i in range(5):
        play_one = input("Enter a value: ")
        play_two = input("Enter a value: ")

        is_user_play_different = play_one != play_two
        is_play_equal = play_one == play_two
        if is_play_equal:
            print("winner is leg two")
            player_two_score += 1
        elif is_user_play_different:
            print("Thw winner is leg one")
            player_one_score += 1

    print("Leg one score is ", player_one_score)
    print("Leg two score is ", player_two_score)


def tired_class():
    print('We are tired!!!!')
    print("Let us go on break!!!!!")
