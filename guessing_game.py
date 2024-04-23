import random
import sys

def main_code():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        attempts += 1  # Increment attempts by 1 for each guess
        guess = input("Guess the number (between 1 and 100) or type 'q' to quit: ")
        
        if guess.lower() == 'q':
            sys.exit("Goodbye!")
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if guess == number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < number:
            print(f'Number is too low. Attempts: {attempts}')
        else:
            print(f'Number is too high. Attempts: {attempts}')
    return attempts

def player_info():
    num_players = int(input("Enter the number of players: "))
    num_rounds = int(input("Enter the number of rounds: "))

    scores = [0] * num_players
    total_attempts = [0] * num_players

    for round_num in range(1, num_rounds + 1):
        print(f"Round {round_num}:")
        round_attempts = [0] * num_players
        for player in range(num_players):
            print(f"Player {player + 1}:")
            attempts = main_code()  # Call main_code instead of guess_number
            round_attempts[player] = attempts
            total_attempts[player] += attempts
        max_attempts = max(round_attempts)
        for player, attempts in enumerate(round_attempts):
            if attempts == max_attempts:
                scores[player] += 1
    print("Final Scores:")
    for player, score in enumerate(scores):
        print(f"Player {player + 1}: {score} points")
    
    print("\nTotal Attempts:")
    for player, attempts in enumerate(total_attempts):
        print(f"Player {player + 1}: {attempts} attempts")

while True:
    print("Welcome to the guessing game!")
    player_info()
    play_again = input("Would you like to play again? (yes/no) ")
    if play_again.lower() != 'yes':
        break

