# Python Quiz Game


questions = ("What's 2+2?🔢: ",
             "What is a potatato? :🥔",
             "What's the largest ocean in the world?🌊🗺️: ",
             "Which planet is known as the 'Red Planet'?🔴🌍: ",
             "Best anime of all time?📔📺: ")

options = (("A. Window", "B. 22", "C. Fish", "D. 4"),
           ("A. Meat", "B. Vegetable", "C. Fruit", "D. Nut"),
           ("A. Atlantic Ocean", "B. Indian Ocean", "C. Southern Ocean", "D. Pacific Ocean"),
           ("A. Mars", "B. Venus", "C. Mercury", "D. Jupiter"),
           ("A. Solo Leveling", "B. Bleach", "C. One Piece", "D. Naruto"))

answers = ("C", "B", "D", "A", "C")
guesses = []
score = 0
question_number = 0 

for question in questions:
    print("**********************")
    print(question)
    for option in options[question_number]:
        print(option)

    # Validation
    while True: 
        guess = input("Enter (A, B, C, D): ").upper() 
        if guess in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid input pal, try again.")

    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("Well done you got it right!🥳")
    else:
        print("Lock in vro.😒")
        print(f"{answers[question_number]} is the correct answers 🥀")
    question_number += 1

print("-----------------------")
print("        RESULTS         ")
print("-----------------------")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guess: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(question_number) * 100)
print(f"Your score is: {score}%")