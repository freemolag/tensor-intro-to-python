from tensor_intro_to_python.delete_and_count_letters import delete_and_count_letters  # noqa: E501


def test_answer_1():
    assert delete_and_count_letters('аббревиатура') == 'ббревитур, ' \
                                                       'удалено букв: 3'


def test_answer_2():
    assert delete_and_count_letters('Все счастливые семьи похожи '
                                    'друг на друга, каждая несчастливая семья '
                                    'несчастлива '
                                    'по-своему.') == 'Все счстливые семьи' \
                                                     ' похожи друг н друг, ' \
                                                     'кждя несчстливя семья ' \
                                                     'несчстлив по-своему., ' \
                                                     'удалено букв: 9'
