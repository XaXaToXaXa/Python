# Task_1 Напишите программу, которая принимает на вход строку и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
"""
input_text = "a a a b c a a d c d d a c b d a"
text_list = input_text.split()
new_list = []
for i in range(len(text_list)):
    if text_list[i] in text_list[:i]:
        new_list.append(text_list[i] + "_" + str(text_list[:i].count(text_list[i]))) #.count выводит номер элемента
    else:
        new_list.append(text_list[i])
print(", " .join(new_list)) # .join добавляет элемент
"""
"""
s = input("Введите строку: ")
words = s.split()
char_count = {}
for word in words:
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

print("Результат подсчета символов:")
for char, count in char_count.items():
    print(f"{char}: {count}")
"""
# Task 2
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
#
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
#
# Output: 13
"""
input_text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".lower()
print(len(set(input_text.split())))
# .lower() убирает регистр
# len() - выводит длинну списка, set() - делает из списка множество (в нем нет повторяющихся элементов) .split() - убирает элемент по умолчанию пробел
"""
#Task_3
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

input_number = int(input("Введите целое положитльное число: "))
input_list = []
while input_number != 0:
    input_list.append(input_number)
    input_number = int(input("Введите целое положитльное число: "))
print(f"Максимальное число из указаных: {max(input_list)}") 

# Ex 1 output 0
# n = int(input())
# max_number = 1000
# while n != 0:
#     n = int(input())
#     if max_number > n:
#         max_number = n
# print(max_number)

# Ex 2 output n
# n = int(input())
# max_number = -1
# while n < 0:
#     n = int(input())
#     if max_number < n:
#         n = max_number
# print(n)