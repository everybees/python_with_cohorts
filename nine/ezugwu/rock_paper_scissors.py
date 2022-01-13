count1 = 0
count2 = 0
# counter =0
# while counter < 10:
for i in range(2):
    female_player = input('Female Player,Enter your choice from rock,paper and scissor:')
    male_player = input('Male Player,Enter your choice from rock,paper and scissor:')
    if female_player == 'rock' and male_player == 'scissor':
        count1 += 1

    if female_player == 'paper' and male_player == 'rock':
        count1 += 1

    if female_player == 'scissor' and male_player == 'paper':
        count1 += 1

    if female_player == 'scissor' and male_player == 'rock':
        count2 += 1

    if female_player == 'rock' and male_player == 'paper':
        count2 += 1

    if female_player == 'paper' and male_player == 'scissor':
        count2 += 1

    if female_player == male_player: print('it is a draw')


print("Male player has ",count1,"points")
print("Dammy has ",count2,"points")


