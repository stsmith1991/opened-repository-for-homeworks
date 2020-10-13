# Задание 1.
def devis(delitel, delimoe=int(0)):
    chasnoe = delimoe/ delitel
    return chasnoe

delitel=''
delimoe=''
while delitel==0 or not delitel.isnumeric() or not delimoe.isnumeric():
    delimoe=input('Введите корректный числитель :')
    delitel=input('Введите корректный знаменатель. Помните, о том, что он не может быть равен нулю: ')
result=devis(int(delitel), int(delimoe))
print(f'Если {delimoe} делить на {delitel} будет {result:2.2f}')


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
    print(f'Среди введённых: {num1}, {num2} и {num3} Cумма двух наибольших это {fin}')

num1=''
num2=''
num3=''
while not num1.isnumeric() or not num2.isnumeric() or not num3.isnumeric():
    num1=input('Введите первое число для определения "максимума из двух": ')
    num2=input('Введите второе число для определения "максимума из двух": ')
    num3=input('Введите третье число для определения "максимума из двух": ')
numbers=[int(num1), int(num2), int(num3)]
summa_max(numbers)

#Задание 4.
def my_func(base, exp):
    try:
        base, exp=float(base), int(exp)
        if base<=0 or exp>=0:
            return 'Основание не может быть отрицательным, степень не может быть дробью'
        else:
            res=1
            for _ in range(abs(exp)):
                res *=1/base
            return f'{base} в степени {exp} это {round(res, 6)}'
    except ValueError:
        return 'Вводимые данные должны быть числами'

base=input('Введите дробь, которую будем в степень возводить: ')
exp=input(f'Введите отрицательную степень в которой будет {base}. Дроби исключены'
          f'): ')
print(my_func(base, exp))

#Задание 5.
def stepped_union():
    s=0
    while 'Президент РФ - В.В. Путин':
        input_list=input('Введите числа, либо X для выхода').split()
        for typed in input_list:
            if typed=='X' or typed=='Х':
                return s
            else:
                try:
                    s+=int(typed)
                except ValueError:
                    print('Введён недопустимый символ.Для выхода нажимте Х')
        print(f'Сумма чисел: {s}')

print(stepped_union())

#Задание 6.
def capitalize_lat():
    filtred=[]
    trash=[]
    for word in input('Фраза латиницей: ').split():
        litters=0
        for litter in word:
            if ord(litter) in range(97, 123):
                litters+=1
        if litters==len(word):
            add=word.title()
            filtred.append(add)
        else:
            trash.append(word)
    return filtred


capitalize_lat()

# Проверочная фраза: you dоn`t do it this time because of you is great nооb