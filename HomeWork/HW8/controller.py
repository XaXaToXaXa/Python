from GUI import *
from Functions import *

def control():
    while True:
        path = 'file.txt'
        req = request()
        if req == 1:
            contact = save_data()
            write_data(path, contact)
        elif req == 2:
            string = output()
            print(read_string(path, string))
        elif req == 3:
            string = output()
            contacts = change_data(path, string)
            new_data(path, contacts)
        elif req == 4:
            parametr = sort_parametr()
            sort(path, parametr)
        elif req == 5:
            print_data()
        elif req == 6:
            string = output()
            contacts = delete_data(path, string)
            new_data(path, contacts)
        elif req == 7:
            break
        else:
            req = int(input('Повторите ввод: '))


        



