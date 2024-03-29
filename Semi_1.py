"""
1. За день машина проезжает n километров.
Сколько дней нужно, чтобы проехать маршрут длиной m километров?
При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

**Input:**

n = 700

m = 750

**Output:**
"""
# n = 700
# m = 750
#
# print(m // n + 1 % (m % n + 1))
"""
2. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
Выведите наименьшее число парт, которое нужно приобрести для них.

**Input:**

20

21

22

**Output:**

32
"""

# a = 20
# b = 21
# c = 22
# o = a+b+c
# o1 = o%2
#
# print(o//2+o1)
# print(a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)

"""
5. Вагоны в электричке пронумерованы натуральными числами, начиная с 1
(при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка).
В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил,
что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке.
Напишите программу, которая будет это делать или сообщать,
что без дополнительной информации это сделать невозможно.
"""

# FindVagon = int(input("Введите вагон, в который сел Витя: "))
# searchNumberVagon = int(input("Введите число вагона, который обнаружил Витя: "))
# totalCountVagon = FindVagon + searchNumberVagon - 1
# if (FindVagon == searchNumberVagon):
#     print("Нехватка данных")
#
# else:
#     print(totalCountVagon)

"""
7. Дано натуральное число. Требуется определить,
является ли год с данным номером високосным.
Если год является високосным, то выведите YES, иначе выведите NO.
Напомним, что в соответствии с григорианским календарем,
год является високосным, если его номер кратен 4,
но не кратен 100, а также если он кратен 400.
"""

# year=int(input("Введите год: "))

# if (year%400==0):
#     print("Yes")
#
# elif(year%4==0 and year%100!=0):
#     print("Yes")
#
# else:
#     print("No")