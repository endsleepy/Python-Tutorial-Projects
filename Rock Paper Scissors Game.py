import random


def game():
    options = ("rock", "paper", "scissors")
    flag = True

    while flag:

        player = None 
        computer = random.choice(options) 

        while player not in options:
            player = input("Enter a choice (rock, paper, scissors)🪨 📃 ✂️ : ")

        print("")
        print(f"👶 You: {player}")
        print(f"🖥️ Computer: {computer}")

        if player == computer:
            print("you TIED! 😭")
        elif player == "rock" and computer == "scissors":
            print("You win!!🥳")
        elif player == "paper" and computer == "rock":
            print("You win!!🥳")
        elif player == "scissors" and computer == "paper":
            print("You win!!🥳")
        else:
            print("Vro you some booty cheeks 💩 How you loosing to a bot😭 ✌️ ☠️ 🥀")

    #   if input("Play again? (y/n): ).lower() == "y": -- Faster way of doing it   
        play_again = input("Wanna play again? (y/n): ").lower()
        if not play_again == "y":
            flag = False  

    print("####################################################################")
    print("###################### Thanks for playing 💖 ######################")
    print("####################################################################")


print("#### ROCK 🪨 #####################################")
print("############### PAPER 📃 #########################")
print("########################## SCISSORS ✂️############")

game("")