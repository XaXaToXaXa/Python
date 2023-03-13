# Задача №31.
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
#
#
# def fibo(num):
#     if num in [0, 1]:
#         return 1
#     return fibo(num - 1) + fibo(num - 2)
#
# fib_num = int(input("Какое число Фибоначчи ищем: "))
# print(f"Искомое числло: {fibo(fib_num)}")
#
# Задача №33.
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
#
# def make_journal(x):
#     journal = [int(input()) for i in range(x)]
#     return journal
#
# def swap_mark(lst):
#     maxx = max(lst)
#     minn = min(lst)
#     for i in range(len(lst)):
#         if lst[i]==minn:
#             lst[i]=maxx
#     return lst
#
# n = int(input())
# print(swap_mark(make_journal(n)))
#
# Задача №35.
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

#
# n = int(input("Введите число: "))
# def simpl(x):
#     count = 0
#     for i in range(1, x+1):
#         if x % i == 0:
#             count += 1
#     if count > 2:
#         print("No")
#     else:
#         print("Yes")
#
#
# simpl(n)
#
# Задача №37.
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3
#
n = int(input("Введите число N: "))
def rec(x):
    if x == 0:
        print(" ")
        return 0
    else:
        print(x, end=" ")
        rec(x-1)
    print(x, end=" ")
rec (n)



