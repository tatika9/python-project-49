import prompt


def start_game(game):
    NUMBER_MIN = 1
    NUMBER_MAX = 100
    ROUND_COUNT = 3

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)

    for _ in range(ROUND_COUNT):
        question, correct_answer = game.generation(NUMBER_MIN, NUMBER_MAX)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
