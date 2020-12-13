class  Warehouse:
    wid = 0
    storage = {}
    title = ['Код', 'Произ-ль', 'Модель', 'Цена', 'Форматы', 'Печать:кач.', 'Печ.:с-ть', 'Печ.:цвет', 'Скан.:кач.',
             'Скан.:с-ть', 'Скан.:цвет']


    def recive(self, equipment, quantity):
        if self.storage.get(equipment) is None:
            self.storage.update({equipment: quantity})
        else:
            self.storage.update({equipment: self.storage.pop(equipment) + quantity})
        print(f'{quantity} {equipment.inf[1]} {equipment.inf[2]}')

    def deport(self, equipment, quantity):
        if self.storage.get(equipment) is None:
            print('Такого нет на складе')
        elif self.storage[equipment] - quantity == 0:
            self.storage.pop(equipment)
        else:
            self.storage.update({equipment: self.storage.pop(equipment) - quantity})
        print(f'{quantity} {equipment.inf[1]} {equipment.inf[2]} удалено')
        print('удалён последний' if self.storage.get(equipment) is None else f'осталось {self.storage.get(equipment)}')

    def __str__(self):
        print(f'Колич-во|' + '|'.join(f'{el:10}' for el in self.title) + '|')
        for key in self.storage.keys():
            print('-' * 130)
            print(f'{self.storage.get(key):8}|', end='')
            print(key)
        return ''


class Unit:
    inf = []

    def __str__(self):
        return '|'.join(f'{el:10}' if el is not None else f'{"None":10}' for el in self.inf) + '|'

    def validate(self):
        if not isinstance(self.inf[3], (int, float)):
            print(f'Задана неверная цена {self.inf[1]} {self.inf[2]}')
            self.inf[3] = None
        if not isinstance(self.inf[5], (int, float, type(None))):
            print(f'Не может существовать такого разрешения печати {self.inf[1]} {self.inf[2]}')
            self.inf[5] = None
        if not isinstance(self.inf[7], (int, float, type(None))):
            print(f'Не может существовать такая скорость печати {self.inf[1]} {self.inf[2]}')
            self.inf[7] = None
        if not isinstance(self.inf[8], (int, float, type(None))):
            print(f'Не может существовать такого разрешения сканирования {self.inf[1]} {self.inf[2]}')
            self.inf[8] = None
        if not isinstance(self.inf[10], (int, float, type(None))):
            print(f'Не может существовать такой скорости сканирования {self.inf[1]} {self.inf[2]}')
            self.inf[10] = None


class Printer(Unit):
    def __init__(self, equip_id, price, developer, model, print_ppi, print_speed, print_color=False, sheet_type='A4, A5'):
        self.inf = [equip_id, developer, model, price, sheet_type, print_ppi, print_color, print_speed, None, None,
                    None]
        super().validate()


class Scanner(Unit):
    def __init__(self, equip_id, price, developer, model, scan_ppi, scan_speed, scan_color=False, sheet_type='A4'):
        self.inf = [equip_id, developer, model, price, sheet_type, None, None, None, scan_ppi, scan_color, scan_speed]
        super().validate()


class MFP(Unit):
    def __init__(self, equip_id, price, developer, model, print_ppi, print_speed, scan_ppi, scan_speed,
                 print_color=False, scan_color=False, sheet_type='A4'):
        self.inf = [equip_id, developer, model, price, sheet_type, print_ppi, print_color, print_speed, scan_ppi,
                    scan_color, scan_speed]
        super().validate()


a = Printer('1', 'fd', 'Epson', 'Coolpix80', 350, 2.5, True)
b = Scanner('2', 4800, 'Xerox', 'X380', 300, 1.5, False)
c = MFP('3', 14500, 'Canon', 'SX8800', 480, 4.3, 600, 3.8, True, True, 'A3')
first = Warehouse()
first.recive(a, 3)
first.recive(b, 10)
first.recive(c, 7)
print(first)
a.inf[3] = 6000
first.deport(a, 2)
first.deport(b, 8)
first.deport(c,7)
print(first)