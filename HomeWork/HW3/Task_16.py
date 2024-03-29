# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1
#Вариант с заданным массивом.
"""
list_size = int(input("Введите размер массива: "))
find_num = int(input("Введите искомое значение: "))
num_list = []
count = 0
for i in range(list_size):
    num_list.append(int(input("Введите натуральное число: ")))
    if find_num == num_list[i]:
        count = count+1
print(f"В массиве :{num_list} число: {find_num} встречается: {count} раз.")
"""
#Вариант с рандомным массивом.

import random
list_size = int(input("Введите размер списка: "))
find_num = int(input("Введите искомое значение: "))
num_list = []
for i in range(list_size):
    num_list.append(random.randint(1, 5))
print(f"В списке :{num_list} число: {find_num} встречается: {num_list.count(find_num)} раз.")
