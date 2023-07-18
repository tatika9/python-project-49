import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def even(number):
    return 'yes' if number % 2 == 0 else 'no'


def generation(NUMBER_MIN, NUMBER_MAX):
    number = random.randint(NUMBER_MIN, NUMBER_MAX)
    correct_answer = even(number)
    return number, correct_answer
