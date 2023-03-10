# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random


def fill_list(size):
    new_list = []
    for i in range(size):
        new_list.append(random.randint(1, 20))
    return new_list



size = int(input("Введите количество кустов: "))
bush_list = fill_list(size)
print(f"На кустах растет: {bush_list} ягод.")
if size <= 3:
    print(sum(bush_list))
else:
    result = 0
    for i in range(size):
        summ = bush_list[i-1] + bush_list[i] + bush_list[(i+1)%size]
        if summ > result: 
            result = summ
            temp = (i-1, i, (i+1)%size)
    print(f"Максимально модуль сможет собрать: {result}")