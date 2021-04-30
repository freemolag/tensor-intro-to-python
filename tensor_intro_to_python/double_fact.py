"""
Дано натуральное число n. Надо вычислить его двойной факториал
"""


def double_fact(n):
    if n <= 0:
        return 1
    return n * double_fact(n-2)
