# Python Quiz Game

# Questions asked to the user
questions = ("What's 2+2?🔢: ",
             "What is a potatato? :🥔",
             "What's the largest ocean in the world?🌊🗺️: ",
             "Which planet is known as the 'Red Planet'?🔴🌍: ",
             "Best anime of all time?📔📺: ")

# Options for the user to pick from
options = (("A. Window", "B. 22", "C. Fish", "D. 4"),
           ("A. Meat", "B. Vegetable", "C. Fruit", "D. Nut"),
           ("A. Atlantic Ocean", "B. Indian Ocean", "C. Southern Ocean", "D. Pacific Ocean"),
           ("A. Mars", "B. Venus", "C. Mercury", "D. Jupiter"),
           ("A. Solo Leveling", "B. Bleach", "C. One Piece", "D. Naruto"))

answers = ("C", "B", "D", "A", "C") # Answers for the questions
# Placeholder variables
guesses = []
score = 0
question_number = 0 

# ------------------------ START OF QUIZ ------------------------
# Loop through questions
for question in questions:
    print("**********************")
    print(question)
    for option in options[question_number]:
        print(option)

    while True: 
        # Asks the user to pick from (A, B, C, D) options
        guess = input("Enter (A, B, C, D): ").upper() # Makes sure the answer is in uppercase
        if guess in ["A", "B", "C", "D"]: # If guess is one of those options break out of loop
            break
        else: # If guess isn't A, B, C, D asks the user for input again
            print("Invalid input pal, try again.")

    # Adds the guess to the guess
    guesses.append(guess)
    # If guess was right
    if guess == answers[question_number]:
        score += 1
        print("Well done you got it right!🥳")
    # If guess was wrong
    else:
        print("Lock in vro.😒")
        print(f"{answers[question_number]} is the correct answers 🥀")
    question_number += 1

# ------------------------ RESULTS ------------------------
# Prints result header
print("-----------------------")
print("        RESULTS         ")
print("-----------------------")

# Diplays correct answers
print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

# Displays the user's guesses
print("guess: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

# Calculates and prints final score
score = int(score / len(question_number) * 100)
print(f"Your score is: {score}%") # Displays final score