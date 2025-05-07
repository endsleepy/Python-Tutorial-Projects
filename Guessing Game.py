import random 

# Python Guessing Game
def game():
    # Define range for number
    lowest_num = 5
    highest_num = 110
    # Randomizing answer
    answer = random.randint(lowest_num, highest_num)
    guesses = 0
    is_running = True # Flag to keep game running
    
    # Prints game header
    print("#######################################################")
    print("############# Python Number Guessing Game #############")
    print("#######################################################")
    print(f"Select a number between {lowest_num} and {highest_num}")

    is_running = True
    while is_running:

        print("") # Blank line for better readability 
        # Ask's the user for their guess
        guess = input("Enter your guess: ")

        try:
            # Trys to convert guess into an integer
            guess = int(guess)
            guesses += 1 # Incriments guess by 1
        except ValueError:
            # If guess is not a number it shows error message
            print("Invalid guess")
            print(f"Select a number between {lowest_num} and {highest_num}")
        else:
            # Checks if guess is out of range
            if guess < lowest_num or guess > highest_num:
                print("That number is out of range vro. Lock in plz! 💩")
                print(f"Select a number between {lowest_num} and {highest_num}")
            # Checks if guess is too loww
            elif guess < answer:
                print("Too low! Try again!")
            # Checks if guess is to high
            elif guess > answer:
                print("Too high! Try again!")
            else:
                # If guess is correct
                print("")
                print("###################################################")
                print(f"WWW YOU GOT IT RIGHT🥳!!! The answer was {answer}")
                print(f"It took you {guesses} trys. Have a nice day!")
                print("###################################################")
                is_running = False # End of game

game()