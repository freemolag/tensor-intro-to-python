from tensor_intro_to_python.words_count import words_count


def test_answer_1():
    assert words_count('') == 0


def test_answer_2():
    assert words_count('111') == 1


def test_answer_3():
    assert words_count('Подсчитать количество слов в строке') == 5
