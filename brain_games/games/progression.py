import random


RULES = 'What number is missing in the progression?'


def generation(NUMBER_MIN, NUMBER_MAX):
    STEP_MIN = 1
    STEP_MAX = 10
    ELEMENT_COUNT_MIN = 5
    ELEMENT_COUNT_MAX = 10

    number_start = random.randint(NUMBER_MIN, NUMBER_MAX)
    step = random.randint(STEP_MIN, STEP_MAX)
    elements = random.randint(ELEMENT_COUNT_MIN, ELEMENT_COUNT_MAX)
    element_list = []
    for _ in range(elements):
        number_start += step
        element_list.append(str(number_start))
    missing_index = random.randint(0, elements - 1)
    correct_answer = str(element_list[missing_index])
    element_list[missing_index] = '..'
    question = ' '.join(element_list)
    return question, correct_answer
