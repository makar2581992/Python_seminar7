def mod():
    mod = input('Выберите режим работы: найти в справочнике - 1, внести данные в справочник - 2: ')
    return mod

def inpp():
    str_person = input('Введите данные через запятую (ФИО, номер телефона, комментарий(по необходимости)): ')
    return str_person

def get_data():
    get_data = input('Выберите вариант поиска: по фамилии - 1, по имени - 2: ')
    return get_data

def exp():
    second_name = input('Введите фамилию человека: ')
    return second_name

def name():
    first_name = input('Введите имя человека: ')
    return first_name
    