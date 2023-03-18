def new_data(path, contacts):
    with open(path, 'w') as data:
        for i in contacts:
            data.write(f'{i}\n')

def write_data(path, contact):
    with open(path, 'a') as data:
        for i in contact:
            data.write(f'{i} ')

def read_data(path):
    with open(path, 'r') as data:
        contacts = data.readlines()
    contacts = [i.strip() for i in contacts]
    return contacts

def read_string(path, string):
    contacts = read_data(path)
    for i in contacts:
        if string in i:
            result = i
    return result

def change_data(path, string):
    contacts = read_data(path)
    for i in range(len(contacts)):
        if string in contacts[i]:
            print(contacts[i])
            r = int(input('Хотите изменить этот контакт?\n Введите 0, чтобы удалить.\n Введите 1, чтобы продолжить поиск\n: '))
            if r == 0:
                print('Измените контакт')
                surname = input('Введите фамилию: ')
                name = input('Введите имя: ')
                number = input('Введите телефон: ')
                contacts[i] = f'{surname} {name} {number}'
                break
        elif i == len(contacts) -1:
            print('Контакт не найден!')
            print()
    return contacts

def sort(path, parametr):
    if parametr in range(0,2):
        contacts = read_data(path)
        contacts = sorted(contacts, key = lambda x: x.split()[parametr])
        with open('file.txt', 'w') as data:
            for i in contacts:
                print(i)
                data.write(f'{i}\n')
    else:
        print('Некорректный выбор.')

def delete_data(path, string):
    contacts = read_data(path)
    for i in range(len(contacts)):
        if string in contacts[i]:
            print(contacts[i])
            r = int(input('Хотите удалить этот контакт?\n Введите 0, чтобы удалить.\n Введите 1, чтобы продолжить поиск\n: '))
            if r == 0:
                contacts.remove(contacts[i])
                break
            print()
        elif i == len(contacts) -1:
            print('Контакт не найден!')
            print()
    return contacts

