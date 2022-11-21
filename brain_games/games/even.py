import random


def generation():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    number_min = 1
    number_max = 100
    count_round = 3
    question_answer = []
    for _ in range(count_round):
        number = random.randint(number_min, number_max)
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        question_answer.append([number, correct_answer])
    return rules, question_answer
