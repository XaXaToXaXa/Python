# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

inputNumber = int(input("Введите количество сделанных журавликов: "))
# boys = (inputNumber//3)/2
# girl = (inputNumber//3)*2
print(f"Из {inputNumber} сделаных журавликов, Катя сделала {(inputNumber//3)*2}, а мальчики по {(inputNumber//3)//2}")

print(f"Из {inputNumber} сделаных журавликов, Катя сделала {(inputNumber//3)*2}, а мальчики по {inputNumber//6}")
print(f"Петя: {inputNumber//6}, Катя: {(inputNumber//3)*2}, Сережа: {inputNumber//6}")