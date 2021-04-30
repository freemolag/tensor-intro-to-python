from tensor_intro_to_python.double_fact import double_fact


def test_answer_1():
    assert double_fact(0) == 1


def test_answer_2():
    assert double_fact(5) == 15


def test_answer_3():
    assert double_fact(10) == 3840
