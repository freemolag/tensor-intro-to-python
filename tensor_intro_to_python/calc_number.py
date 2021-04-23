"""
При заданном целом числе n посчитайте n + nn + nnn
"""


def calc_number(n):
    double_n = str(n) * 2
    triple_n = str(n) * 3
    return n + int(double_n) + int(triple_n)
