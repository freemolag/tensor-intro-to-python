"""
Для каждого числа от 1 до 100,
вывести список чисел меньше текущего и кратного 5
"""


def div_five(first, second):
    list_range = list(range(first, second))
    i = first
    while i <= second:
        filtered = list(filter(lambda x: x % 5 == 0 and x < i, list_range))
        print(f'{i} {filtered}')
        i += 1
    return 'Finish!'
