import random


def generation():
    RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
    NUMBER_MIN = 1
    NUMBER_MAX = 100
    ROUND_COUNT = 3
    question_answer = []
    for _ in range(ROUND_COUNT):
        number = random.randint(NUMBER_MIN, NUMBER_MAX)
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        question_answer.append([number, correct_answer])
    return RULES, question_answer
