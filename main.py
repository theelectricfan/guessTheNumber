import os
import random
from arts import logo
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def game():
    ans = random.randint(1, 100)
    clear_screen()
    print(logo)
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100 (1 and 100 included).")
    print("You have to try to guess it.")
    difficulty = input("Choose a difficulty: type 'easy' or 'hard': ").lower()

    invalid = True
    attempts = -1
    while invalid:
        if difficulty == 'easy':
            attempts = 10
            invalid = False
        elif difficulty == 'hard':
            attempts = 5
            invalid = False
        else:
            print("Invalid input! Try again.")

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > ans:
            print("My number is lower.")
            attempts -= 1
        elif guess < ans:
            print("My number is higher.")
            attempts -= 1
        else:
            print(f"You got it. My number was {ans}")
            break

    if attempts <= 0:
        print("You have run out of guesses. You lose.")
        print(f"My number was {ans}")


play = 'y'
while play == 'y':
    game()
    play = ''
    while play != 'y' and play != 'n':
        play = input("Would you like to play another game. Type 'y' or 'n': ")
        if play != 'y' and play != 'n':
            print("Invalid input! Try again.")
