# 4.11 (Guess-the-Number Modification) Modify the previous exercise to count the number of guesses the player makes.
# If the number is 10 or fewer, display "Either you know the
# secret or you got lucky!" If the player makes more than 10 guesses, display "You should
# be able to do better!" Why should it take no more than 10 guesses? Well, with each “good
# guess,” the player should be able to eliminate half of the numbers, then half of the remaining
# numbers, and so on. Doing this 10 times narrows down the possibilities to a single number.
# This kind of “halving” appears in many computer science applications. For example, in the
# “Computer Science Thinking: Recursion, Searching, Sorting and Big O” chapter,
# we’ll present the high-speed binary search and merge sort algorithms, and you’ll attempt the quicksort
# exercise—each of these cleverly uses halving to achieve high performance.
import random

value = random.randrange(1, 1001)
declaration = ""
count = 0
counter = 0
while counter != 1:
    guess = int(input("Enter your guess: "))
    if guess == value:
        print("Congratulations! You guessed the number")
        count += 1
        counter += 1
    elif guess < value:
        print("Too low. Try again")
        count += 1
    elif guess > value:
        print("Too high. Try again")
        count += 1

if counter <= 10:
    print("Either you know the secret or you just got lucky")
if counter > 10:
    print("You should be able to do better than that")