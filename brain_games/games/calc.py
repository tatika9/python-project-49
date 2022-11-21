import random


def generation():
    RULES = 'What is the result of the expression?'
    NUMBER_MIN = 1
    NUMBER_MAX = 100
    ROUND_COUNT = 3
    OPERATOR_ALL = ['+', '-', '*']
    question_answer = []
    for _ in range(ROUND_COUNT):
        number1 = random.randint(NUMBER_MIN, NUMBER_MAX)
        number2 = random.randint(NUMBER_MIN, NUMBER_MAX)
        operator = random.choice(OPERATOR_ALL)
        question = f'{number1} {operator} {number2}'
        correct_answer = str(eval(question))
        question_answer.append([question, correct_answer])
    return RULES, question_answer
