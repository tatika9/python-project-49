import random


def gcd(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 >= number2:
            number1 %= number2
        else:
            number2 %= number1
    return number1 or number2


def generation():
    rules = 'Find the greatest common divisor of given numbers.'
    number_min = 1
    number_max = 100
    count_round = 3
    question_answer = []
    for _ in range(count_round):
        number1 = random.randint(number_min, number_max)
        number2 = random.randint(number_min, number_max)
        question = f'{number1} {number2}'
        correct_answer = str(gcd(number1, number2))
        question_answer.append([question, correct_answer])
    return rules, question_answer
