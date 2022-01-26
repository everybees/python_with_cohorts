user_input = input("Car Menu: ").lower()
if user_input == 'help':
    print("""
        start ==> To start the car
        stop  ==> To stop the car
        quit ==> To quit the game
        """)
    user_input_from_menu = input()

while user_input_from_menu!= 'quit':
    if user_input_from_menu == 'start':
        print('Car has started!')
    elif user_input_from_menu == 'stop':
        print ('Car has stopped, press start to restart!')
    elif user_input_from_menu != 'start' or user_input_from_menu != 'stop':
        print('invalid command, Try again')
    user_input_from_menu = input()