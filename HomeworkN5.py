from dicts import russian
# Задание 1
def recive_eng():
    print('')
    return

print('Задание 1')
with open(r"user_data.txt", "w", encoding="utf-8") as my_f:
    glavlist = []
    im = str('не пусто')
    while im != "":
        im = input('Тут ввести всё, что желаем видеть в "text.txt". Если (больше) ничего не желаем, жмём Enter:')
        glavlist.append(im)
    print(glavlist)
    my_f.writelines([str(i) for i in glavlist])

print('Задание 2')
#Задание 2.
with open("text.txt", "r", encoding="utf-8") as my_f:
    sub_content=my_f.readlines()
    if len(sub_content)==0:
        print('Файл пуст. Ноль строк, ноль знаков.')
    else:
        content=[el[0:-1] for el in sub_content]    # Элементы списка open содержат /n в своём конце. Они путают счёт
        print('Всего строк в файле: ', len(content))
        n_str=1
        for i in content:
            print(f'В строке №{n_str} - {len(i)} знак(ов);')
            n_str+=1

print('Задание 3')
#Задание 3.
with open("text_3.txt", "r", encoding="utf-8") as f:
    anything=f.readlines()
    cut_a_edgs=[k[0:-1] for k in anything]     # Элементы списка, возвращённого open содержат /n в своём конце.
    sub_splited_one=[]
    sub_splited_all=[]
    staff_wage={}
    for el in cut_a_edgs:
        sub_splited_one= el.split()
        sub_splited_all.append(sub_splited_one)
    for i in sub_splited_all:
        staff_wage.update({i[0]:float(i[1])})
        for staff, wage in staff_wage.items():
            if wage<20000:
                print('Среди бедняг-работяг: ', staff)
average=sum(staff_wage.values())/len(staff_wage.values())
print('"Голубцы, которые все, в среднем, едят" cоставляет (ден.ед.):', average)

#Задание 4.
print('\nЗадание 4.')
with open("text_04.txt", "r", encoding="utf-8") as f:
        all_str = f.readlines()
        cut_a_edgs = [k.replace('\n', "") for k in all_str]  # Элементы списка, возвращённого open содержат /n в своём конце.
        spllited=[]
        sub_split=[]
        english={}
        for thing in cut_a_edgs:
            sub_split=thing.split(' — ')
            spllited.append(sub_split)
        for couple in spllited:
            english.update({couple[0]:couple[1]})
        final = {key: value for key, value in zip(russian.keys(), english.values())}
        print('Переведённый исходный файл имеет вид:\n')
