from tensor_intro_to_python.parse_filename import parse_filename


def test_answer_1():
    assert parse_filename(r"C:\development\inside\test-project\inside\myfile.txt") == 'myfile'   # noqa: E501
