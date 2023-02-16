# print (5)
# print (5)
# print (5)

# a = 5
# b = 5.89
# c = 'Hello'

# print (f"{a} и {b} и еще {c}")
# print ("{} -{} - {}".format(a,b,c))

# a = input ("Введи что нибудь: ")
# print (f" Ты ввел {a}")
# print ("Введи что нибудь еще: ")
# b = input ()
# print (f"Сложениее первого и второго = { int(a) + int(b)}")

# a = 5.65464
# b = 4.543
# print (round(a*b, 3))

# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# n = 423
# summa = 0
# while summa > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa) # 9

# i = 0
# while i < 5:
#     if i == 3:
#         # break
#         i = i + 1
# else:
#     print('Пожалуй')
#     print('надоело')
# print(i)

# n = 423
# summa = 0
# while summa > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(summa)
# # Пожалуй
# # хватит )
# # 9

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1