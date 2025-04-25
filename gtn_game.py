# Guess The Number Game
# Computer picks a random number between 1 and 100
# You try to guess it
# After each guess, the computer tells you if your guess is too high, too low, or correct
# The game ends when you guess the right number

import random

secret_number = random.randint(1, 100)

player_guess = None

while player_guess != secret_number:
    player_guess = int(input("Guess a number between 1 and 100: "))

    if player_guess < secret_number:
        print("Too Low!")
    elif player_guess > secret_number:
        print("Too High!")
    else:
        print("You got it!")


