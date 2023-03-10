# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
#
# *Пример:*
#
# ноутбук
#     12


# English letters
"""
import re
input_word = input("Введите слово: ")
diction = {'[AaEeIiOoUuLlNnSsTtRr]': '1', '[DdGg]': '2', '[BbCcMmPp]': '3',
           '[FfHhVvWwYy]': '4', 'Kk': '5', '[JjXx]': '8', '[QqZz]': '10'}
for key in diction:
    input_word = re.sub(key, diction[key], input_word)
print(sum(map(int, input_word)))
"""

# Русские буквы
diction = {'АаВвЕеИиНнОоРрСсТт': 1, 'ДдКкЛлМмПпУу': 2,
           'БбГгЁёЬьЯя': 3, 'ЙйЫы': 4, 'ЖжЗзХхЦцЧч': 5, 'ШшЭэЮю': 8, 'ФфЩщЪъ': 10}


def scrabble(letter):
    for key in diction:
        if letter in key:
            return diction.get(key)


input_word = input("Введите слово: ")

print(f"Вы набрали {sum(map(scrabble, input_word))} очков")
