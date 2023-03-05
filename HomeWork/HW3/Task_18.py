# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

# Вариант с последовательным массивом.
""""
def fill_list(size):
    new_list = []
    for i in range(size):
        new_list.append(int(input("Введите натуральное число: ")))
    return new_list
"""
# Рандом
import random

def fill_list(size):
    new_list = []
    for i in range(size):
        new_list.append(random.randint(1, 20))
    return new_list


list_size = int(input("Введите размер массива: "))
find_num = int(input("Введите искомое значение: "))

my_list = fill_list(list_size)
closest_num = my_list[0]
for i in my_list:
    if abs(i-find_num) <= abs(closest_num-find_num):
        closest_num = i
   

print(f"В массиве :{my_list} ближайшее число к: {find_num} является: {closest_num}.")
