import random
from tkinter import N
# roll 2 dice and return their faces
def roll_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2) #pack die faces into tuple

def display_dice(dice):
    die1, die2 = dice #unpacking tuple
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')

sides_rolled =roll_dice()
display_dice(sides_rolled)

# detrmine pts
sum_of_dice = sum(sides_rolled)
if sum_of_dice in (7, 11):
    game_status = 'WON'
elif sum_of_dice in (2, 3, 12):
    game_status ='LOST'
else: 
    game_status = 'CONTINUE'
    point = sum_of_dice
    print('Point is ', point)
while game_status == 'CONTINUE':
    sides_rolled =roll_dice()
    display_dice(sides_rolled)
    sum_of_dice = sum(sides_rolled)

if sum_of_dice == point:
    game_status ='WON'
elif sum_of_dice == 7:
    game_status ='LOST'


