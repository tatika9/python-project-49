import random


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def generation():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    number_min = 1
    number_max = 100
    count_round = 3
    question_answer = []
    for _ in range(count_round):
        number = random.randint(number_min, number_max)
        if is_prime(number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        question_answer.append([number, correct_answer])
    return rules, question_answer
