class Wear:
    def __init__(self, size, h):
        self.size = size
        self.h = h

    @property
    def calc(self):
        if self.h is None:
            res = f'Потребуется {round(self.size / 6.5 + 0.5, 3)} ткани'
        elif self.size is None:
            res = f'Потребуется {round((self.h / 2) * 0.3)} ткани'
        else:
            res = f'Скрипт сломан'
        return res


class Coat(Wear):
    def __init__(self, size, h):
        Wear.__init__(self, size, h)


class Combine(Wear):
    def __init__(self, size, h):
        Wear.__init__(self, size, h)


bathcoat = Coat(size=26, h=None)
covall = Combine(h=184, size=None)
print(bathcoat.calc)
print(covall.calc)
