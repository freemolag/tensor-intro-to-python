"""
Для каждого числа от 1 до 100,
вывести список чисел меньше текущего и кратного 5
"""


def div_five(first, second):
    L = list(range(first, second))
    n = first
    new_list = []
    for i in L:
        while n < i:
            if n % 5 == 0:
                new_list.append(n)
                print(f'{i} {new_list}')
                n += 1
            else:
                print(f'{i} {new_list}')
                n += 1
    return 'Finish!'
