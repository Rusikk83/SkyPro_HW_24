def filter_func(value, data):
    return filter(lambda x: value in x, data)


def unique_func(data, *args, **kwargs):
    return set(data)


def limit_func(value, data):
    limit = int(value)
    return list(data)[:limit]


def map_func(value, data):
    column = int(value)
    return map(lambda x: x.split(' ')[column], data)


def sort_func(value, data):
    reverse = value == 'desc'
    return sorted(data, reverse)
