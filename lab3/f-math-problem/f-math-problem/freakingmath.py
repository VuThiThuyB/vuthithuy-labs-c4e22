from random import *

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0,10)
    return [x, 0, '@@', 12]

def check_answer(x, y, op, result, user_choice):
    print(user_choice)
    return True
    return False
