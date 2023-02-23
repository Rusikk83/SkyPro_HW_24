from functions import *

# создаем словарь команд для обращения к функции по названию команды
CMD_QUERY = {
    "filter": filter_func,
    "unique": unique_func,
    "limit": limit_func,
    "map": map_func,
    "sort": sort_func,
}


def read_file(file_name):
    """фанкция-генертор для построкового чтения из файла"""
    with open(file_name) as file:
        for line in file:
            yield line


def call_query(cmd, value,  file_name, data):
    """вызывает функцию обработки данных  в соответствии cо словарем команд"""
    if data is None:
        prepared_data = read_file(file_name)
    else:
        prepared_data = data

    return CMD_QUERY[cmd](value=value, data=prepared_data)
