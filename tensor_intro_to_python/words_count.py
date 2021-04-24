"""
Подсчитать количество слов в строке
"""


def words_count(string):
    if string == '':
        return 0
    return len(string.split(' '))
