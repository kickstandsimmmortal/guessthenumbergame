# Guess The Number Game
# Computer picks a random number between 1 and 100
# You try to guess it
# After each guess, the computer tells you if your guess is too high, too low, or correct
# The game ends when you guess the right number

import random

while True:
    secret_number = random.randint(1, 100)
    difficulty = input("Choose a difficulty: easy, normal, or hard: ").lower()

    if difficulty == "easy":
        max_guesses = None
    elif difficulty == "normal":
        max_guesses = 10
    elif difficulty == "hard":
        max_guesses = 3
    else:
        print("Invalid difficulty selected. Defaulting to normal")
        max_guesses = 10

    player_guess = None
    guess_count = 0
    
    while True:
        player_guess = int(input("Guess a number between 1 and 100: "))
        guess_count += 1

        if player_guess < secret_number:
            print("Too Low!")
        elif player_guess > secret_number:
            print("Too High!")
        else:
            print("You got it!")
            break

        if max_guesses is not None and guess_count >= max_guesses:
            print(f"Out of guesses! The number was {secret_number}. Game over.")
            break
    
    play_again = input("Want to play again? Enter yes or no: ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
    