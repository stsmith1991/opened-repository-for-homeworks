# Задание 1
hat_keys = str('данное')
hat_values = str('возвращаемое type()')
number_var = int(8)
pi_var = float(3.14)
complex_var = complex(8.1)
union_var = str((number_var, pi_var, complex_var))
inspection = dict(var_int=type(number_var), var_float=type(pi_var), var_complex=type(complex_var))
print('Типы единичных данных в Python:', end='\n')
print(hat_keys, inspection.keys())
print('пример', number_var, pi_var, complex_var)
print(hat_values, inspection.values())

# Задание 2
result_list = list(map(int, input('Введите данные в количестве четырёх: ').split()))
for i in range(1, len(result_list), 2):
    result_list[i - 1], result_list[i] = result_list[i], result_list[i - 1]
print(result_list)

# Задание 3.1 (c помощью list)
m = int(input('Введите порядковый номер месяца : '))
while m not in range(0, 13):
    print('Нет месяца с порядковым номером ', m)
    m = int(input('Введите порядковый номер месяца : '))
t = list('0')
t.append('Январь')
t.append('Февраль')
t.append('Март')
t.append('Апрель')
t.append('Май')
t.append('Июнь')
t.append('Июнь')
t.append('Август')
t.append('Сентябрь')
t.append('Октябрь')
t.append('Ноябрь')
t.append('Декабрь')
i = 'Не задал'
if m in range(1, 3) or m == 12:
    i = 'Зима'
elif m in range(3, 6):
    i = 'Весна'
elif m in range(6, 9):
    i = 'Лето'
elif m in range(9, 13):
    i = 'Осень'
print('Месяц ', t[m], 'соответствует времени года: ', i)

# Задание 4.
word = input('Введите слово(а) через пробел: ').split()
for n, i in enumerate(word, 1):
    print((n, i) if len(i) <= 10 else print(n, (i[:10])))

# Задание 5.
raiting = [9, 8, 7, 7, 7, 6, 5, 3, 3, 3, 2, 1]
addition = int(input('Добавить ещё баллов:'))
i = 0
for new in raiting:
    if addition <= new:
        i += 1
raiting.insert(i, float(addition))
print(raiting)

# Задание 6.
items = []
meta_dump = {'Название': '', 'Стоимость': '', 'Количество': '', 'ед.изм.': ''}
review = {'Название': [], 'Цена': [], 'Количество': [], 'ед.измер.': []}
count = 0
while 'рак на горе не свиснет'.islower() == True:
    if input('Нажмите Х для выхода ').upper() == 'X':
        break
    x_pressed = True
    for meta in meta_dump.keys():
        criteria = input(f'Введите значение назначаемого {meta}: ')
        meta_dump[meta] = int(meta_dump) if (meta == 'Стоимость' or f == 'Количество') else criteria
        review[meta].append(meta_dump[meta])
    items.append((count, meta_dump))
    print(f'\nТовары:\n{items}')
    print(f'\nДанные по товарам\n {"*" * 30}')
    for keys, values in review.items():
        print(f'{key[:25] > 30}: {value}')
    print("*" * 30)
