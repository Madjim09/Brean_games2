MAX_ROUNDS = 3

def run_game(game):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.RULE)

    for _ in range(MAX_ROUNDS):
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")