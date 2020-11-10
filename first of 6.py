from time import sleep

class Trafficlight:
    __color=0

    def running(self):
        lights = [{
                'name':'красный',
                'color':'\x1b[42m',
                'delay':7
            },
            {   'name': 'жёлтый',
                'color': '\x1b[43m',
                'delay': 2
            },
            {   'name': 'зелёный',
                'color': '\x1b[42m',
                'delay': 5
            }
        ]
        while True:
            tl=''
            for i in range(3):
                if i==self.__color:
                    tl+=f'({lights[self.__color]["color"]}  \x1b(0m)'
                else:
                    tl+='(  )'
            print(f'\r{tl}', end='')
            sleep(lights[self.__color]['delay'])
            self.__color=(self.__color+1)%3

lights=Trafficlight()
lights.running()