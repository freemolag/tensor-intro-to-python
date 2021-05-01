from tensor_intro_to_python.change_list import change_list


def test_answer_1():
    assert change_list([1, 2, 10, 5, 7]) == [10, 2, 1, 5, 7]
