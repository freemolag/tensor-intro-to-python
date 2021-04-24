"""
В строке удалить все буквы "а" и подсчитать количество удаленных символов
"""


def delete_and_count_letters(string):
    letters = list(string)
    delete_letters = list(filter(lambda x: x != 'а', letters))
    new_string = ''.join(delete_letters)
    count_letters = letters.count('а')
    return f'{new_string}, удалено букв: {count_letters}'
