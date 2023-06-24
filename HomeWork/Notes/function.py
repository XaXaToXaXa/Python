import file_operation
import note
import ui

number = 3  # сколько знаков МИНИМУМ может быть в тексте заметки


def add():
    record = ui.create_note(number)
    array = file_operation.read_file()
    for notes in array:
        if note.Note.get_id(record) == note.Note.get_id(notes):
            note.Note.set_id(record)
    array.append(record)
    file_operation.write_file(array, 'a')
    print('Запись внесена.')


def show(text):
    logic = True
    array = file_operation.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in note.Note.get_date(notes):
                print(note.Note.map_note(notes))
    if logic:
        print('Записей нет.')


def id_edit_del_show(text):
    id = input('Введите id записи: ')
    array = file_operation.read_file()
    logic = True
    for notes in array:
        if id == note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                record = ui.create_note(number)
                note.Note.set_title(notes, record.get_title())
                note.Note.set_body(notes, record.get_body())
                note.Note.set_date(notes)
                print('Запись изменена.')
            if text == 'del':
                array.remove(notes)
                print('Запись удалена.')
            if text == 'show':
                print(note.Note.map_note(notes))
    if logic == True:
        print('Записи нет, попробуйте другой id')
    file_operation.write_file(array, 'a')
