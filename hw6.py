class Road:
    th = 1
    __length = 5000
    __width = 25

    def __calc(self):
        m = int(self.__length) * int(self.__width) * int(self.th)
        print(f'Для дороги длинной и шириной {self.__length}х{self.__width} метров и толщиной {self.th} см потребуется '
              f'{m} килограмм асфальта')


my_r = Road()
try:
    my_r._Road__length = int(input("Введите длинну дороги, м.\n"))
    my_r.th = input("Толщина покрытия, см.\n")
    my_r._Road__calc()
except ValueError:
    print('Введено некорректное значение. Расчёт произведён из значений по умолчанию')
    my_r._Road__calc()
