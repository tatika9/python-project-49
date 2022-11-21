import random


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def generation():
    RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    NUMBER_MIN = 1
    NUMBER_MAX = 100
    ROUND_COUNT = 3
    question_answer = []
    for _ in range(ROUND_COUNT):
        number = random.randint(NUMBER_MIN, NUMBER_MAX)
        if is_prime(number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        question_answer.append([number, correct_answer])
    return RULES, question_answer
