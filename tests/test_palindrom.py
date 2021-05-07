from tensor_intro_to_python.is_palindrom import is_palindrom


def test_answer_1():
    assert is_palindrom(121) is True


def test_answer_2():
    assert is_palindrom(1331) is True


def test_answer_3():
    assert is_palindrom(1333) is False
