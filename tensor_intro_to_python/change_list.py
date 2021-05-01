"""
поменяйте местами самый большой и саый маленький элемент списка
"""


def change_list(numbers):
    new_list = numbers
    max_num = max(numbers)
    min_num = min(numbers)
    max_index = numbers.index(max_num)
    min_index = numbers.index(min_num)
    new_list[max_index] = min_num
    new_list[min_index] = max_num
    return new_list
