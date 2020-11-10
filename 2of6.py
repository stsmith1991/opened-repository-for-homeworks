class Stationery:
    def __init__(self, title):
        self.title = title

    def drow(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def drow(self):
        print('Уникальное сообщение')


class Pencil(Stationery):
    def drow(self):
        print('Другое уникальное сообщение')


class Handle(Stationery):
    def drow(self):
        print('Да, сегодня у меня с фантазией беда просто =)')


penal = Stationery('просто для проверки наследования')
red = Pen('красный цвет')
blue = Pencil('синий цвет')
green = Handle('зелёный')
red.drow()
blue.drow()
green.drow()
