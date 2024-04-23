import random
import sys


while True:  # this loop is to make the game repeatable
    tries = 0
    number = 0
    max_tries = 0
    number = random.randint(1, 100)
    print("Welcome to guess game.")
    print("If you want to quit type q.")
    print("If you want to start over type r.")
    while True:  # chacks for right variable
        max_tries = input("Whats the number of max attempts you want to have: ")
        if max_tries.lower() == "q":  # completly ends the game
            sys.exit()
        elif max_tries.lower() == "r":  # restarts the game
            continue
        try:
            max_tries = int(max_tries)
        except ValueError:
            print("thats not a number")
        else:
            break
    while max_tries > tries:
        guess = input("Enter a number from 1-100: ")  # you dont need to include it all ifs
        if guess.lower() == "q":  # completly ends the game
            sys.exit()
        elif guess.lower() == "r":  # restarts the game
            break
        try:
            guess = int(guess)
        except ValueError:
            print("thats not a number")
            continue
        tries += 1
        if guess > number:
            print(f'number is too high,attempts {tries}')
        elif guess < number:
            print(f'number is too small,attempts {tries}')
        else:
            print(
                f'Correct, you found the number!!: {number}\n\n')  # no need for othe if since its already part of the while
            break
    if max_tries <= tries:
        print("Game over you lose because you reached the max number of attempts")
        print(f"The number was: {number}\n\n")


