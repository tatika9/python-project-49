import random


def gcd(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 >= number2:
            number1 %= number2
        else:
            number2 %= number1
    return number1 or number2


def generation():
    RULES = 'Find the greatest common divisor of given numbers.'
    NUMBER_MIN = 1
    NUMBER_MAX = 100
    ROUND_COUNT = 3
    question_answer = []
    for _ in range(ROUND_COUNT):
        number1 = random.randint(NUMBER_MIN, NUMBER_MAX)
        number2 = random.randint(NUMBER_MIN, NUMBER_MAX)
        question = f'{number1} {number2}'
        correct_answer = str(gcd(number1, number2))
        question_answer.append([question, correct_answer])
    return RULES, question_answer
