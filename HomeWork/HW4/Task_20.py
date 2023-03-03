# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

def fill_list(size):
    new_list = []
    for i in range(size):
        new_list.append(int(input("Enter number: ")))
    return new_list


first_size = int(input("Enter 1 list size : "))
firs_list = fill_list(first_size)
second_size = int(input("Enter 2 list size: "))
second_list = fill_list(second_size)

print(f"Sorted list: {sorted(set(firs_list+second_list))}")