import random


def generation():
    rules = 'What is the result of the expression?'
    number_min = 1
    number_max = 100
    count_round = 3
    question_answer = []
    operator_all = ['+', '-', '*']
    for _ in range(count_round):
        number1 = random.randint(number_min, number_max)
        number2 = random.randint(number_min, number_max)
        operator = random.choice(operator_all)
        question = f'{number1} {operator} {number2}'
        correct_answer = str(eval(question))
        question_answer.append([question, correct_answer])
    return rules, question_answer
