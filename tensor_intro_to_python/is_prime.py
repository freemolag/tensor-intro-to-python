"""
Вывести список простых чисел до 1000.
Число простое, если оно имеет только 2 делителя (1 и само себя).

is_prime.py - функция определяющая является ли число простым
prime_numbers.py - функция которая выводит список простых чисел
"""


def is_prime(num):
    if num < 2:
        return False
    i = 2
    while i < num:
        if num % i == 0:
            return False
            i += 1
        else:
            i += 1
    return True
