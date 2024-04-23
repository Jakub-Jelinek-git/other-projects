import random
import sys

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = input("Guess the number (between 1 and 100) or type 'q' to quit: ")
        if guess.lower() == 'q':
            sys.exit("Goodbye!")
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        attempts += 1
        if guess == number:
            print("Congratulations! You guessed the number.")
            break
        elif guess < number:
            print("Try higher.")
        else:
            print("Try lower.")
    return attempts

def player_info():
    num_players = int(input("Enter the number of players: "))
    num_rounds = int(input("Enter the number of rounds: "))

    scores = [0] * num_players

    for round_num in range(1, num_rounds + 1):
        print(f"Round {round_num}:")
        round_attempts = []
        for player in range(num_players):
            print(f"Player {player + 1}:")
            attempts = guess_number()
            round_attempts.append(attempts)
        max_attempts = max(round_attempts)
        for player, attempts in enumerate(round_attempts):
            if attempts == max_attempts:
                scores[player] += 1

    print("Final Scores:")
    for player, score in enumerate(scores):
        print(f"Player {player + 1}: {score} points")

while True:
    print("Welcome to the guessing game!")
    player_info()
    play_again = input("Would you like to play again? (yes/no) ")
    if play_again.lower() != 'yes':
        break
