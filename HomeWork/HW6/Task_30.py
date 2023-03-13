# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


def ar_subs (n, a1, d):
    result = []
    for i in range(n):
        result.append(a1 + i * d)
    return result 

subs_size = int(input("Введите размер последовательности: "))
subs_first_number = int(input("Введите первое число последовательности: "))
subs_diff = int(input("Введите шаг последовательности: "))

print(f"Арифметическая погрессия : {ar_subs(subs_size, subs_first_number, subs_diff)}")     
