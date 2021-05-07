from tensor_intro_to_python.is_palindrom import is_palindrom


def test_answer_1():
    assert is_palindrom(121) == True


def test_answer_2():
    assert is_palindrom(1331) == True

def test_answer_2():
    assert is_palindrom(1333) == False
