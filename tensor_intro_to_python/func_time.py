"""
Напишите декоратор func_time, который подсчитывает  и выводит сколько времени выполняется функция, обернутая в него.
"""

import time
from tensor_intro_to_python.amount_lucky import amount_lucky

def func_time(fn):
    def wrapper():
        start_time = time.time()
        fn()
        print("Функция some_func выполнялсь %s сек" % (time.time() - start_time))
    return wrapper

@func_time
def some_func():
    amount_lucky()

# some_func() 
