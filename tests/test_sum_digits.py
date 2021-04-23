from tensor_intro_to_python.sum_digits import sum_digits


def test_answer_1():
    assert sum_digits(0) == 0


def test_answer_2():
    assert sum_digits(111) == 3


def test_answer_3():
    assert sum_digits(348) == 15
