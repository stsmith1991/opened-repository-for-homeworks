from functools import reduce
from sys import argv
from random import randint
from itertools import islice, cycle, count


def randomize():
    randlist = [randint(0, 25) for el in range(randint(5, 17))]
    return randlist


'''Вставляет на место размещения список случайной длинны со случайными целыми числами'''


# Задание 1.
def wage():
    try:
        hours, hour_price, adv = map(float, argv[1:])
        print(f'Зарплата составляет: {hours * hour_price + adv}')
    except ValueError:
        print('Введите все три числовых параметра.')


wage()

# Задание 2.
original_list = randomize()
original_list.insert(0, int(0))
my_list = [original_list[i] for i in range(len(original_list)) if original_list[i] > original_list[i - 1]]
print(my_list)

# Задание 3.
print([u for u in range(20, 241) if u % 20 == 0 or u % 21 == 0])

# Задиние 4.
natural_list = randomize()
print([z for z in natural_list if natural_list.count(z) == 1])

# Задание 5.
row = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(lambda f, s: f * s, row))


# Задание 6.
def clone(start, finish, loops):
    try:
        start, finish, loops = int(start), int(finish), int(loops)
        initial = [el for el in islice(count(), start, finish + 1)]
        iteration = iter(el for el in cycle(initial))
        clone_list = [next(iteration) for _ in range(loops)]
        print(initial)
        return clone_list
    except ValueError:
        return "Введено недопустимое значение"
    except TypeError:
        return "У вас опечатка"


print(clone(input('Введите число с которого начнём'), input("Введите число, которым закончим"),
            input("повторов изначальнго цикла: ")))


# Задание 7.
def factorial(n):
    first_ = 1
    if n == 0:
        yield f"{n} =1"
    for i in range(1, (n + 1)):
        first_ *= 1
        yield f'{i}!={first_}'


for el in factorial(int(input('X!='))):
    print(el)
