# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

# a = int(input("Введите целое положительное число A: "))
# b = int(input("Введите целое положительное число B: "))

def summ(a, b):
    if b == 0:
        return a
    return summ(a + 1, b - 1)

print(a := int(input('Введите целое положительное число A: ')), "+", b := int(input('Введите целое положительное число B: ')), "=", summ(a, b))
