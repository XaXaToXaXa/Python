# Task 1
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
#
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
#
# Output: 6
"""
num_list = [1, 1, 2, 0, -1, 3, 4, 4]
new_list = set(num_list) # переводим в множество (оно содержит только уникальные элементы)

print(f'В списке {num_list} -->> {len(new_list)} значений являются уникальными')
"""
# Task 2
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
#
# Input: [1, 2, 3, 4, 5] k = 3
#
# Output: [4, 5, 1, 2, 3]
"""
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
num_shift = 3
new_list = []

for i in range(-num_shift, len(num_list) - num_shift): # Переносим последнии элементы с индексом смещения
    new_list.append(num_list[i])                       # Собираем поэлементно начиная с первого элемента уходящего на круг

# первая часть отсекает К элементов с конца и переносит их в начало, вторая часть отступает К элементов с начала
# new_list = num_list[-num_shift:] + num_list[:-num_shift]

print(f'Для списка {num_list} новый список со смещение {num_shift} равен {new_list}')
"""

# Доп задачи
# Создайте список из случайных чисел.
# Найдите номер его последнего локального максимума
# (локальный максимум — это элемент, который больше любого из своих соседей).
"""
import random

num_list = []
max = 0
for i in range(8):
    num_list.append(random.randint(1, 20))
print(f"Cписок из случайных чисел. {num_list}")
#Проверка идет от 2 элемента до предпоследнего
for i in range(1, len(num_list)-1): 
    if num_list[i - 1] < num_list[i] > num_list[i + 1]:
        max = i
print(f"Номер его последнего локального максимума {max + 1}")
"""
# Создайте список из случайных чисел. Найдите второй максимум.
#
# a = [1, 2, 3] # Первый максимум == 3, второй == 2
"""
import random

num_list = []
max = 0
max2 = 0

for i in range(8):
    num_list.append(random.randint(1, 20))
print(f"Cписок из случайных чисел. {num_list}")

for i in num_list:
    if i > max:
        max2 = max
        max = i
    elif i > max2 and i != max:
        max2 = i
print(max2)
"""
# Task 3
# Напишите программу для печати всех уникальных значений в словаре.
#
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
#
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""
dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "},
        {" VIII ": " S007 "}]
# res = []
# for elem in dict:           # Просмотр словаря
#     elems = elem.values()   # Просмотр значения, для просмотра ключа указать keys
#     for i in elems:
#         i = i.strip(' ')    #Отсечение лишнего знака от элемента
#         if i not in res:
#             res.append()    # Сохранение элементов в список

res = set([value.strip() for lst in dict for value in lst.values()])
print(res)
"""
# Task 4
# Дан массив, состоящий из целых чисел. Напишите программу,
# которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)
#
# Input: [0, -1, 5, 2, 3]
#
# Output: 2
#
# Пояснение: (-1 < 5, 2 < 3)
"""
import random

num_list = []
for i in range(10):
    num_list.append(random.randint(1, 20))
print(f"Cписок из случайных чисел. {num_list}")

counter = 0

for i in range(1, len(num_list)):           #Подсчет через цикл
    if num_list[i - 1] < num_list[i]:
        counter += 1

print(counter)
"""
