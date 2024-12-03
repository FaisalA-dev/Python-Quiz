# This is my Python Trivia game. It will quiz you on some facts and give you a percentage grade in the end.
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score(correct_guesses, guesses):
    print("------------------------")
    print("YOUR RESULTS")
    print("------------------------")

    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")


def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.lower()
    if response == "yes":
        return True
    else:
        return False


# -------------------------------------
questions = {
    "What is Python named after?": "A",
    "What is the mascot for Python?": "B",
    "Which keyword is used to define a function in Python?": "A",
    "Who is the owner of Tesla?": "A",
}

options = [
    ["A. Monty Python", "B. The snake", "C. Bill Gates", "D. Elon Musk"],
    ["A. A turtle", "B. A snake", "C. A tiger", "D. A spider"],
    ["A. def", "B. func", "C. method", "D. idk"],
    ["A. Elon Musk", "B. George Washington", "C. Faisal Anwari", "D. Bill Gates"],
]

while True:
    new_game()
    if not play_again():
        break
