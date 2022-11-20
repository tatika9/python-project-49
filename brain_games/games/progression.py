import random


def generation():
    rules = 'What number is missing in the progression?'
    number_min = 1
    number_max = 100
    step_min = 1
    step_max = 10
    elements_min = 5
    elements_max = 10
    count_round = 3
    question_answer = []
    for _ in range(count_round):
        number_start = random.randint(number_min, number_max)
        step = random.randint(step_min, step_max)
        elements = random.randint(elements_min, elements_max)
        element_list = []
        for _ in range(elements):
            number_start += step
            element_list.append(str(number_start))
        missing_index = random.randint(0, elements - 1)
        correct_answer = str(element_list[missing_index])
        element_list[missing_index] = '..'
        question = ' '.join(element_list)
        question_answer.append([question, correct_answer])
    return rules, question_answer
