"""
Напишите функцию, которая подсчитывает количество счастливых
шестизначных билетов.
Билеты начинаются с 000000 и заканчиваются 999999.
Счастливым считается билет, если сумма первых трех значений,
равна сумме вторых трёх (Например: 927864, 123006, 002110 и т.д.)

разбить на 2 списка цифр
найти сумму каждого из  них
сравнить
"""


from functools import reduce


def summ(digits):
    return reduce(lambda x, y: int(x) + int(y), digits)


def is_lucky(num):
    first_digits = str(num)[:3]
    second_digits = str(num)[3:]
    if summ(first_digits) == summ(second_digits):
        return True
    return False


def amount_lucky():
    i = 0
    n = 0
    while i <= 999999:
        if is_lucky(str(i).zfill(6)):
            n += 1
            i += 1
        else:
            i += 1
    return n
