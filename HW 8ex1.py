class StringDate:
    def __init__(self, date):
        self.date = date

    @classmethod
    def flech(cls, date):
        date.replace('0', '')
        return [int(i) for i in date.split('-')]

    @staticmethod
    def val(pamparam):
        if 2000 <= pamparam[2] <= 2020:
            even_mounth = [1, 3, 5, 7, 8, 10, 12]
            if 1 <= pamparam[1] <= 12:
                if pamparam[1] in even_mounth and pamparam[0] in range(1, 32):
                    print(f'Дата \n{pamparam}\nис вэлид')
                elif pamparam[1] == 2:
                    if pamparam[0] == 29 and ((pamparam[2] % 4 == 0 and pamparam[2] % 100 != 0) or (pamparam[2] % 400 == 0)):
                        print(f'Дата \n{pamparam}\nис вэлид')
                    elif pamparam[0] > 28:
                        print(f'Нет {pamparam[0]} числа в феврале')
                    else:
                        print(f'Дата \n{pamparam}\nис вэлид')
                elif pamparam[1] in [4, 6, 9, 11] and pamparam[0] in range(1, 31):
                    print(f'Дата \n{pamparam}\nис вэлид')
                else:
                    print(f'Нет {pamparam[0]}-ого дня в {pamparam[1]}-ом месяце')
                    if pamparam[0] >= 31 and pamparam[1] in [6, 7, 8]:
                        print('А жаль =(')
            else:
                print(f'Нет {pamparam[1]} месяца в году')
        else:
            print('Давайте вернёмся в это двадцатилетие (2000-2020г.г.)')


date_in_row = input('Введите дату в формате "дд-мм-гггг":\n')
try:
    obj = StringDate.flech(date_in_row)
except Exception:
    print('Нет. Перезайдите и введите (адекватную) дату в формате дд-мм-гггг')
try:
    print(StringDate.val(obj))
except NameError:
    print('')
