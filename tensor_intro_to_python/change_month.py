from datetime import datetime


def change_month(date_str, m):
    d = datetime.strptime(date_str, '%d.%m.%y')
    new_month = (((d.month - 1) + m) % 12) + 1
    new_year = d.year + (((d.month - 1) + m) / 12)
    new_date = datetime.strptime(f'{d.day}.{new_month}.{int(new_year)}',
                                 '%d.%m.%Y')
    return new_date.strftime("%d.%m.%y")
