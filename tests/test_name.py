from tensor_intro_to_python.name import Name


obj = Name('Иванов', 'Иван', 'Иванович')


def test_action():
    assert obj.brief_name() == 'Иванов Иван'


def test_action2():
    assert obj.initials() == 'Иванов И. И.'


def test_action3():
    assert obj.strfname('%И %О %ф.') == 'Иван Иванович И.'


def test_action4():
    assert obj.strfname('%и. %о. %Ф') == 'И. И. Иванов'
