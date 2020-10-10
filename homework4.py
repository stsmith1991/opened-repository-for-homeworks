from functools import reduce
from sys import argv

# Задание 1.
def imported():
    scr_name, profit, hour_price, adv = argv
    result = int(profit) * int(profit) + adv
    return result


# Задание 2. Рэндомизировать список
original_list =  [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
original_list.insert(0, int(0))
my_list = [original_list[i] for i in range(len(original_list)) if original_list[i] > original_list[i - 1]]
print(my_list)

# Задание 3.
print([u for u in range(20, 241) if u % 20 == 0 or u % 21 == 0])

# Задиние 4. Рэндомизировать исходный, упихать в одну строку
natural_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([z for z in natural_list if natural_list.count(z) == 1])

# Задание 5.
row = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(lambda f, s: f * s, row))
