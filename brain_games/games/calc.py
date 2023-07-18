import random


RULES = 'What is the result of the expression?'


def generation(NUMBER_MIN, NUMBER_MAX):
    OPERATOR_ALL = ['+', '-', '*']
    number1 = random.randint(NUMBER_MIN, NUMBER_MAX)
    number2 = random.randint(NUMBER_MIN, NUMBER_MAX)
    operator = random.choice(OPERATOR_ALL)
    question = f'{number1} {operator} {number2}'
    correct_answer = str(eval(question))
    return question, correct_answer
