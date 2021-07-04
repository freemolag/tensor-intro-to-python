from tensor_intro_to_python.change_month import change_month


def test_answer_1():
    assert change_month('12.12.12', 7) == '12.07.13'


def test_answer_2():
    assert change_month('01.11.10', -5) == '01.06.10'
