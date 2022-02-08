import random
from random import Random

randoms = random.randrange(1, 1001)

userInput = int(input('Guess the number between 1 and 1000 with the fewest guesses'))

while userInput != randoms:
    if userInput == randoms:
        print('Congratulations. You guessed the number ')
    elif userInput > randoms:
        print('Too High Try Again')
    elif userInput < randoms:
        print("Too low. Try again")
    userInput = int(input('Guess the number between 1 and 1000 with the fewest guesses'))