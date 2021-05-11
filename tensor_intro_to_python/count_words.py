"""
Напишите функцию. На вход подается строка (текст), на выходе должен быть
словарь,где ключ – это слово, а значение – число: сколько раз данное слово
повторилось в тексте (регистр не имеет значения).
"""
from collections import Counter
import re


def count_words(text):
    words = re.sub(r"[^\w\s]", "", text).split()
    lower_case_words = list(map(lambda x: x.lower(), words))
    return Counter(lower_case_words)
