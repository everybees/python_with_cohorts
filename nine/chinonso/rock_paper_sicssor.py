
# bella = input('Bella,Enter your choice from rock,paper and scissor:')
# dammy = input('Dammy,Enter your choice from rock,paper and scissor:')
# if bella == 'rock' and dammy == 'scissor':print('Bella win')
# if bella == 'paper' and dammy == 'rock':print('Bella win')
# if bella == 'scissor' and dammy == 'paper':print('Bella win')
# if bella == 'scissor' and dammy == 'rock':print("Dammy win")
# if bella == 'rock' and dammy == 'paper':print('Dammy win')
# if bella == 'paper' and dammy == 'scissor':print('Dammy win')
# if bella == dammy:print('it is a draw')


count1 = 0
count2 = 0
# counter =0
# while counter < 10:
for i in range(10):
    bella = input('Bella,Enter your choice from rock,paper and scissor:')
    dammy = input('Dammy,Enter your choice from rock,paper and scissor:')
    if bella == 'rock' and dammy == 'scissor':
        count1 += 1
        # print('Bella win')

    if bella == 'paper' and dammy == 'rock':
        count1 += 1
        # print('Bella win')

    if bella == 'scissor' and dammy == 'paper':
        count1 += 1
        # print('Bella win')

    if bella == 'scissor' and dammy == 'rock':
        count2 += 1
        # print("Dammy win")

    if bella == 'rock' and dammy == 'paper':
        count2 += 1
        # print('Dammy win')

    if bella == 'paper' and dammy == 'scissor':
        count2 += 1
        # print('Dammy win')

    if bella == dammy: print('it is a draw')


print("Bella has ",count1,"points")
print("Dammy has ",count2,"points")


