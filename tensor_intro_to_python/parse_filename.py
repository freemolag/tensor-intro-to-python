"""
Дана строка, содержащая полное имя файла (например,
'C:\development\inside\test-project\inside\myfile.txt').  # noqa: W605
Выделите из этой строки имя файла без расширения.
"""


def parse_filename(string):
    file_ext = string.split('\\')
    filename = file_ext[-1].split('.')
    return filename[0]
