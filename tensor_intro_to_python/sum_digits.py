"""
Сложите цифры целого числа
"""
from functools import reduce


def sum_digits(number):
    split_number = [int(i) for i in str(number)]
    return reduce(lambda x, y: x + y, split_number)
