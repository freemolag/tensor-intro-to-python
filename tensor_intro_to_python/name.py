

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


a = Name('Иванов', 'Иван', 'Иванович')
b = Name('Петров', 'Олег')
