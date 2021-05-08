from tensor_intro_to_python.is_prime import is_prime


def test_answer_1():
    assert is_prime(3) is True


def test_answer_2():
    assert is_prime(21) is False


def test_answer_3():
    assert is_prime(10) is False
