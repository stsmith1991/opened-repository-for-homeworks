class CustomError(Exception):
    def __init__(self, txt):
        self.txt = txt

    """
    Своё исключение в чистом виде. Вызывается только вручную. В качестве комментария ошибки выводит первый агрумент
    """


print('Введите одно число')
numbers = []
char = str()
while char != 'stop':
    char = input()
    try:
        if char.isdigit():
            numbers.append(int(char))
            print(f'"{char}"- принято')
        elif char in ['стоп', 'СТОП', 'Стоп', 'stop', 'STOP']:
            break
        elif char != 'stop':
            raise CustomError(f'{char} не число. Отбрасываем.')
    except CustomError as err:
        print(err)
print(numbers)
