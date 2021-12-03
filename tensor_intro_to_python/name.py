"""
Опишите класс Name. Экземпляр класса создается одной строкой,
состоящей из 2-3 слов (на это должна быть проверка).
Например: Name('Иванов Иван') или Name('Иванов Иван Иванович')
Среди методов этого класса должны быть:
    brief_name() - возвращает строку вида 'Фамилия Имя' (без отчества)
    initials() - возвращает строку вида 'Фамилия И.О.'
    strfname(format) - преобразует по переданному формату format строку,
    где %Ф - фамилия, %ф - первая буква фамилии,
    %И - имя, %и - первая буква имени,
    %О - отчество, %о - первая буква отчества
Например: name.strfname('%И %О %ф.') -> Иван Иванович И.
          name.strfname('%и. %о. %Ф') -> И. И. Иванов
"""


class Name:

    def __init__(self, last_name, name, middle_name=''):
        self.last_name = last_name  # фамилия
        self.name = name  # имя
        self.middle_name = middle_name  # отчество

    def brief_name(self):
        return f'{self.last_name} {self.name}'

    def initials(self):
        if self.middle_name == '':
            return f'{self.last_name} {self.name[0]}.'
        return f'{self.last_name} {self.name[0]}. {self.middle_name[0]}.'

    def strfname(self, format):
        for r in (("%И", self.name),
                  ("%О", self.middle_name),
                  ("%ф", f'{self.last_name[0]}'),
                  ("%и", f'{self.name[0]}'),
                  ("%о", f'{self.middle_name[0]}'),
                  ("%Ф", self.last_name)):
            format = format.replace(*r)
        return format
