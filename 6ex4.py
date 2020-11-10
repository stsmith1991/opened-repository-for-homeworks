from time import asctime


class Car:
    def __init__(self, name, color, speed, ispolice):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.ispolice = ispolice

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        self.speed = 0
        print(f'Машина {self.name} остановилась')

    def turn(self, dir):
        self.dir = dir
        print(f'Машина развернулась в сторону {self.dir}')

    def show_speed(self):
        print(f'Скорость машины {self.name} сейчас:{self.speed}')


class TownCar(Car):
    def __init__(self, name, color, speed, ispolice):
        Car.__init__(self, name, color, speed, ispolice)

    def show_speed(self):
        if self.ispolice == False:
            if self.speed > 60:
                print(f'{self.color} {self.name} проехал с недопустимо большой скростью ({self.speed})')
            else:
                print(f'Скорость машины {self.name}:{self.speed}')
        else:
            print(f'Автомобиль {self.name} пронёсся со скоростью {self.speed} с воющей сиреной и мигалкой')


class WorkCar(Car):
    def __init__(self, name, color, speed):
        Car.__init__(self, name, color, speed, ispolice=False)

    def show_speed(self):
        if self.speed > 40:
            print(f'Дорожной технике {self.name} следует ехать медленней!')
        else:
            print(f'скорость дорожной техники {self.name}:{self.speed}')
        return


road_roller = WorkCar('дорожный каток', 'жёлтый', 3)
snow_harvester = WorkCar('снегоуборочный комбайн', 'белый', 5)
sewage_disposal = WorkCar('ассенизаторная машина', 'детской неожиданности', 55)
old_cedan = TownCar('запорожец', 'голубой', 38, False)
fire_fighter = TownCar('пожарная машина', 'красный', 80, True)
luxory_jeep = TownCar('крутой джип', 'чёрный', 70, False)
print(f'Запись из дневника светофора, описанного в первом задании\n{asctime()}, перекрёсток улицы Ленина и Комсомолькой'
      f'\n\tДорогой дневинк. День сегодня задался на удивление собыйнымм! В девять, после того, как {snow_harvester.color}'
      f' {snow_harvester.name} закончил свою работу и укатил в закат')
snow_harvester.show_speed()
print(f'Приехали рабочие на машине с замысловатым названием {road_roller.name}, весь {road_roller.color} и, как это '
      f'принято, в нашей стране,\nпринялись менять дорожное покрытие. Работали быстро, тормозило только их техника.')
print(road_roller.show_speed())
print(f'Свежее дорожное покрытие, припарашиваемое снегом, держалось недолго.')
sewage_disposal.show_speed()
print(f'Помимо того, что при её скорости {sewage_disposal.speed} испортился асфальт, это создало аварийную ситуацию.'
      f'\nЕхавший прямо за ней {old_cedan.name} со скоростью {old_cedan.speed} соскользул в колею и')
old_cedan.turn('встречной полосы.')
print('Водитель не растерялся и выжал ручник на себя.')
old_cedan.stop()
old_cedan.show_speed()
print(f'За секунду до аварии по встречной полосе')
fire_fighter.show_speed()
print(f'Водитель авто {old_cedan.color} {old_cedan.name} перевёл дух и его')
old_cedan.go()
print(f'дальше. До ночи дорого была пуста, кроме того что')
luxory_jeep.show_speed()
