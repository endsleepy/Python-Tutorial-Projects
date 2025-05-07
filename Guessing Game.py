# Python Guessing Game
import random 

def game():
    lowest_num = 5
    highest_num = 110
    answer = random.randint(lowest_num, highest_num)
    guesses = 0
    is_running = True
    
    print("#######################################################")
    print("############# Python Number Guessing Game #############")
    print("#######################################################")
    print(f"Select a number between {lowest_num} and {highest_num}")

    is_running = True
    while is_running:

        print("")
        guess = input("Enter your guess: ")

        try:
            guess = int(guess)
            guesses += 1
        except ValueError:
            print("Invalid guess")
            print(f"Select a number between {lowest_num} and {highest_num}")
        else:
            if guess < lowest_num or guess > highest_num:
                print("That number is out of range vro. Lock in plz! 💩")
                print(f"Select a number between {lowest_num} and {highest_num}")
            elif guess < answer:
                print("Too low! Try again!")
            elif guess > answer:
                print("Too high! Try again!")
            else:
                print("")
                print("###################################################")
                print(f"WWW YOU GOT IT RIGHT🥳!!! The answer was {answer}")
                print(f"It took you {guesses} trys. Have a nice day!")
                print("###################################################")
                is_running = False

game()