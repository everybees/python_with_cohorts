r = 'rock'
p = 'paper'
s = 'scissor'
first_player: str = input("""first player should enter one of the following option:
1.rock 
2.paper 
3.scissor:""")
second_player: str = input("""second player enter one of the following option: 
1.rock 
2.paper 
3.scissor:""")
if first_player == 'rock' and second_player == 'scissor':
    print("first player win!")
elif first_player == 'scissor' and second_player == 'paper':
    print("first player win!")
elif first_player == 'paper' and second_player == 'rock':
    print("first player win!")
elif first_player == second_player:
    print("No wins!, draw draw. ")
else:
    print("Second player wins")