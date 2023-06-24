import note


def create_note(number):
    title = check_len_text_input(
        input('Введите название заметки: '), number)
    body = check_len_text_input(
        input('Введите текст заметки: '), number)
    return note.Note(title=title, body=body)


def menu():
    print("\n       БЛОКНОТ\nИмеются следующие функции:\n\n1: Вывод всех заметок из файла\n2: Добавление записи\n3: "
          "Удаление\n4: Редактирование\n5: Выборка по дате\n6: Выбор по id\n7: Выход\n\nВыберите действие: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} знаков\n')
        text = input('Введите тескт: ')
    else:
        return text


def goodbuy():
    print("Не забывайте про нас.")
