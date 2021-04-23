from tensor_intro_to_python.calc_number import calc_number


def test_answer_1():
    assert calc_number(0) == 0


def test_answer_2():
    assert calc_number(1) == 123


def test_answer_3():
    assert calc_number(9) == 1107
