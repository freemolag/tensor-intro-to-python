from tensor_intro_to_python.phone_check import phone_check


def test_answer_1():
    assert phone_check('8-999-777-77-77') == '89997777777'


def test_answer_2():
    assert phone_check('+7 999 777 77 77') == '79997777777'


def test_answer_3():
    assert phone_check('+7-999-777-77-77') == '79997777777'
