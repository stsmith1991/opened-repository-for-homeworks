# Задание 1.
def devis(synerged=([None], [1])):
    chasnoe = synerged[0] / synerged[1]
    return chasnoe


d_d = [0, 0]
while d_d[1] == 0:
    d_d = list(map(int, input("Введите делимое и делитель через пробел: ").split()))
a = devis(d_d)
print('Результат деления равен ', a)


# Задание 2.
def anceta(f_name, s_name, y_b, sity, email, ph_num):
    print(f'Здравствуй, {f_name} {s_name}, {y_b} года рождения. Теперь, когда я знаю твой родной город - {sity}, твой '
          f'электронный почтовый ящик ({email}) и номер телефона: {ph_num}, я обязательно свяжусь с тобой. До встерчи =)')
    return


carcass = {"f_name": input('Введите имя: '), 's_name': input('Введите фамилию: '), 'y_b': input('Введите ваш г.р.: '),
           'sity': input('Введите город, в котором вы родились: '),
           'e-mail': input('Введите адрес электронной почты: '),
           'ph_num': input('Введите ваш контактный номер телефона: ')}
keys = [carcass.get('f_name')], [carcass.get('s_name')], [carcass.get('y_b')], [carcass.get('sity')], \
       [carcass.get('e-mail')], [carcass.get('ph_num')]
anceta(keys[0], keys[1], keys[2], keys[3], keys[4], keys[5])

#Задание 3.
def summa_max(numbers=list):
    mininal = int(numbers.index(min(numbers)))
    fleching = numbers.pop(mininal)
    fin = sum(numbers)
    print("Cумма двух наибольших: ", fin)
    return fin

[number1, number2, number3] = list(map(int, input("Введите числа:").split()))
numbers=[number1, number2, number3]
summa_max(numbers)

#Задание 4.
