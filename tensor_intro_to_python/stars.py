"""
Вывести на экран циклом N строк из "*", причем каждая строка должна быть
пронумерована и длина строки равна номеру
"""


def stars(maximum):
    i = 1
    while i <= maximum:
        star = '*' * i
        print(f'{i} {star}')
        i += 1
    return('Finish!')
