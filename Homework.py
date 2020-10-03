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
result_list = list(input('Введите данные в количестве четырёх: '))
part_1 = result_list[slice(0, 3, 1)]
rev1 = part_1.reverse()
part_2 = result_list[slice(2, 1, -1)]
rev2 = part_2.reverse()
print(result_list, 'Переворачиваем', part_1, part_2, sep='\n')

# Задание 3.1 (c помощью list)
m = int(input('Введите порядковый номер месяца : '))
while m not in range(1, 12):
    print('Нет месяца с порядковым номером ', m)
    m = int(input('Введите порядковый номер месяца : '))
t = list('')
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
if m in range(1, 2) or m == 12:
    i = 'Зима'
elif m in range(3, 5):
    i = 'Весна'
elif m in range(6, 8):
    i = 'Лето'
elif m in range(9, 11):
    i = 'Осень'
print('Месяц ', t[m], 'соответствует времени года: ', i)

# Задание 3.2 (c помощью dict)
m = int(input('Введите порядковый номер месяца : '))
while m not in range(1, 12):
    print('Нет месяца с порядковым номером ', m)
    m = int(input('Введите порядковый номер месяца : '))
t = {'1': "Январь", '2': "Февраль", '3': "Март", '4': "Апрель", '5': "Май", '6': "Июнь", '7': "Июль", '8': "Август",
     '9': "Сентябрь", '10': "Октябрь", '11': "Ноябрь", '12': "Декабрь"}
for i in t:
    if m in range(t[1], t[2]) or m == t[12]:
        i = 'Зима'
    elif m in range(t[3], t[5]):
        i = 'Весна'
    elif m in range(t[6], t[8]):
        i = 'Лето'
    elif m in range(t[9], t[11]):
        i = 'Осень'
print('Месяц ', t[m], 'соответствует времени года: ', i)

# Задание 4 (Не получается)
# words=list()
# num=int()
# while len(words)!=10:
#    for num in "word":
#        words[int(num)]=list(input('Введите слово'))
#        num+=1
# for int(x) in words:
#    words[int(x)]=words[int(x)].splice[0,11]
# for num in enumerate(words):                              Дальше по плану нумерация, но он вообще не нумерует
