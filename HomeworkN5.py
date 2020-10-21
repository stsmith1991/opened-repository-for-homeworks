from random import randrange, randint
from dicts import russian as rus
#from dicts import lemurian as mur
#from dicts import color as clr
#from dicts import english as  eng

print('Задание 1')
with open(r"user_data.txt", "w", encoding="utf-8") as my_f:
    glavlist = []
    im = str('не пусто')
    while im != "":
        im = input('Тут ввести всё, что желаем видеть в "text.txt". Если (больше) ничего не желаем, жмём Enter:')
        glavlist.append(im)
        glavlist.append('\n')
    my_f.writelines([str(i) for i in glavlist])

print('\nЗадание 2')
# Задание 2.
with open("text.txt", "r", encoding="utf-8") as my_f:
    sub_content = my_f.readlines()
    if len(sub_content) == 0:
        print('Файл пуст. Ноль строк, ноль знаков.')
    else:
        content = [el[0:-1] for el in sub_content]  # Элементы списка open содержат /n в своём конце. Они путают счёт
        print('Всего строк в файле: ', len(content))
        n_str = 1
        for i in content:
            print(f'В строке №{n_str} - {len(i)} знак(ов);')
            n_str += 1

print('\nЗадание 3')
# Задание 3.
with open("text_3.txt", "r", encoding="utf-8") as f:
    anything = f.readlines()
    cut_a_edgs = [k[0:-1] for k in anything]  # Элементы списка, возвращённого open содержат /n в своём конце. Срезаем.
    sub_splited_one = []
    sub_splited_all = []
    staff_wage = {}
    for elt in cut_a_edgs:
        sub_splited_one = elt.split()
        sub_splited_all.append(sub_splited_one)
    for ir in sub_splited_all:
        staff_wage.update({ir[0]: float(ir[1])})
    for staff, wage in staff_wage.items():
        if wage < 20000:
            print('Среди бедняг-работяг: ', staff)
average = sum(staff_wage.values()) / len(staff_wage.values())
print('"Голубцы, которые все, в среднем, едят" cоставляет (ден.ед.):', average)

# Задание 4.
print('\nЗадание 4.')
try:
    dic_lang=int(input('На какой язык будем переводить text_04.txt?\n'
                   '1-русский язык\n'
                   #'2-язык цветов (шуточный)\n'
                   #'3-лемурианский (очень шуточный)\n'
                   #'4-английский\n'
    ))
except TypeError:
    print('\nОшибка ввода. Язык установлен по умолчанию (русский)\n')
    dic_lang= rus
except ValueError:
    print('\nОшибка ввода! Язык установлен по умолчанию (русский)\n')
    dic_lang = rus

def dic(dic_lang):
    if dic_lang==1:
        print('Выбран русский язык')
        lang = rus
    #elif dic_lang==2:
        #print('Выбран язык "цветов"')
        #lang= clr
    #elif dic_lang==3:
        #print('Выбран язык узбагоительного лемура')
        #lang=mur
    #elif dic_lang==4:
        #print('Выбран анлгийский язык. Серьёзно!? С английского на английский?')
        #lang= eng
    #return lang

with open("text_04.txt", "r", encoding="utf-8") as f:
    all_str = f.readlines()
    cut_a_edgs = [k.replace('\n', "") for k in all_str]  # Элементы списка, возвращённого open содержат /n в своём конце
    spllited = []
    sub_split = []
    initial = {}
    f_list=[]
try:
    for thing in cut_a_edgs:
        sub_split = thing.split(' — ')
        spllited.append(sub_split)
    for couple in spllited:
        initial.update({str(couple[1]): couple[0]})
    final = {}
    for iterator in initial:
        if iterator in rus:
            final[iterator] = rus[iterator]
        else:
            print('Ошибка в процессе')
    for y in final.items():
        f_list.append(' — '.join(y))
except IndexError:
    print('\nНекорретно записанные данные. Приведите их в вид "Слово - Цифра"\n')
with open("translated_text_04.txt", "w", encoding="utf-8") as trs:
    for couple in f_list:
        trs.write(couple)
        trs.write('\n')
    trs.close()
    print(f'Переведённый файл выглядит так:')
    print('\n'.join(f_list))
    print('Только что он был записан в translated_text_04.txt в корне настоящего файла.')

#Задание 5.
print('\nЗадание 5.')
with open("ex5.txt",  "w", encoding="utf-8") as text_file:
    row=[randint(0, 50) for _ in range(randrange(1, 200))]
    text_file.write(' '.join(map(str, row)))
    print(f'Сумма элементов сгенерированной строки составляет:{sum(row)}.Саму же строку можно увидеть в файле ex5.txt.')

#Задание 6.
with open("text_6.txt", "r", encoding="utf-8") as file:
    c=file.readlines()
    #for all in c:
        #line=' '.join((l if l else ' ' for l in range(1, 10)) for el in all)
        #replace=[int(i) for i in line.split()]
        #print(f'{all.split()[0]} {sum(replace)}')

#Задание 7.
