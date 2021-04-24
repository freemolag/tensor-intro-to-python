"""
Проверить что номера телефонов состоят только из цифр
"""


def phone_check(number):
    filtered = list(filter(lambda x: x != '+' and x != ' ' and x != '-',
                           list(number)))
    return ''.join(filtered)
