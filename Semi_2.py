# # По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N
# # (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# #
# # Input:       5
# #
# # Output:    120
#
# n=int(input("Введите число: "))
# result=1
# while(n>0):
#     result=n*result
#     n-=1
#
# print(result)
#
# # Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# # то есть выведите такое число n, что φ(n)=A.
# # Если А не является числом Фибоначчи, выведите число -1.
# #
# # Input:     5
# #
# # Output:  6
#
# innumber = int(input("Введите число: "))
# numberFibo1 = 0
# numberFibo2 = 1
# fibo = 0
# count = 2
# while (fibo < number):
#     fibo = numberFibo1+numberFibo2
#     numberFibo1 = numberFibo2
#     numberFibo2 = fibo
#     count += 1
# if (fibo == number):
#     print(count)
# else:
#     print("-1")
#
#
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь,
# занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
# Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50
#
# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2
#
# n = int(input())
# s = list(input().split(' '))
# j = 0
# k = 0
# for i in range(n):
#     a = int(s[i])
#     if a > 0:
#         j = j + 1
#     else:
#         j = 0
#     if j > k:
#         k = j
# print(k)
#
# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
# Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза
# Input:	5 -> 5 1 6 5 9
# Output:	1 9
# def task(ws):
#     mi, ma = ws[0], ws[0]
#     for w in ws:
#         if w > ma:
#             ma = w
#         if w < mi:
#             mi = w
#     return (ma, mi)
#
#
# input()  # пропускаем N
# ws = list(map(int, input().split(" ")))
# print(task(ws))