from functions import *
from typing import Dict, Callable, Iterable,Optional, List, Any
# создаем словарь команд для обращения к функции по названию команды
CMD_QUERY: Dict[str, Callable] = {
    "filter": filter_func,
    "unique": unique_func,
    "limit": limit_func,
    "map": map_func,
    "sort": sort_func,
    "regex": regex_func,
}


def read_file(file_name: str) -> Iterable[str]:
    """фанкция-генертор для построкового чтения из файла"""
    with open(file_name) as file:
        for line in file:
            yield line


def call_query(cmd: str, value: str,  file_name: str, data: Optional[Iterable[str]]) -> Iterable[Any]:
    """вызывает функцию обработки данных  в соответствии cо словарем команд"""
    if data is None:
        prepared_data: Iterable[str] = read_file(file_name)
    else:
        prepared_data = data

    return CMD_QUERY[cmd](value=value, data=prepared_data)
