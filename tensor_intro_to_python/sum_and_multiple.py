"""
найдите сумму и произведение элементов списка
"""


from functools import reduce


def sum_and_multiple(numbers):
    sum_numbers = reduce(lambda x, y: x + y, numbers)
    multiple_numbers = reduce(lambda x, y: x * y, numbers)
    return f'{sum_numbers} and {multiple_numbers}'
