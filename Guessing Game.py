# Python Guessing Game
import random 

def game():
    lowest_num = 5
    highest_num = 110
    answer = random.randint(lowest_num, highest_num)
    guesses = 0
    is_running = True

    print("Python Number Guessing Game")
    print(f"Select a number between {lowest_num} and {highest_num}")

    is_running = True
    while is_running:

        guess = input("Enter your guess: ")

        try:
            guess = int(guess)
            guesses += 1
        except ValueError:
            print("Invalid guess")
            print(f"Select a number between {lowest_num} and {highest_num}")
        else:
            if guess < lowest_num or guess > highest_num:
                print("That number is out of range")
                print(f"Select a number between {lowest_num} and {highest_num}")
            elif guess < answer:
                print("Too low! Try again!")
            elif guess > answer:
                print("Too high! Try again!")
            else:
                print(f"CORRECT! The answer was  {answer}")
                print(f"Number of guesses was {guesses}")
                is_running = False
        
game()