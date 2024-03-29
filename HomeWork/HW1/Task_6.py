# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

inputNumber = input("Введите номер билета: ")
half1 = int(inputNumber[0]) + int(inputNumber[1]) + int(inputNumber[2])
half2 = int(inputNumber[3]) + int(inputNumber[4]) + int(inputNumber[5])
if half1 == half2:
    print("Lucky")
else:
    print("Trash")

secondHalf1 = int(inputNumber) // 1000
secondHalf2 = int(inputNumber) % 1000
secondHalf1 = secondHalf1 // 100 + secondHalf1 // 10 % 10 + secondHalf1 % 10
secondHalf2 = secondHalf2 // 100 + secondHalf2 // 10 % 10 + secondHalf2 % 10
if secondHalf1 == secondHalf2:
    print("Lucky")
else:
    print("Trash")