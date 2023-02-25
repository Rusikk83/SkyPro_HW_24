import re
from typing import Iterable, Any, Set, List, Iterator


def filter_func(value: str, data: Iterable[str]) -> Iterator[str]:
    return filter(lambda x: value in x, data)


def unique_func(data: Iterable[str], *args: Any, **kwargs: Any) -> Set[str]:
    return set(data)


def limit_func(value: str, data: Iterable[str]) -> List[str]:
    limit = int(value)
    return list(data)[:limit]


def map_func(value: str, data: Iterable[str]) -> Iterator[str]:
    column = int(value)
    return map(lambda x: x.split(' ')[column], data)


def sort_func(value: str, data: Iterable[str]) -> List[str]:
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)


def regex_func(value: str, data: Iterable[str]) -> Iterator[str]:
    pattern = re.compile(value)
    return filter(lambda x: re.search(pattern, x), data)
