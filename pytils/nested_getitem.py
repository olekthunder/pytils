def nested_getitem(obj, *keys, default=None):
    """
    >>> nested_getitem({1:{2:{3:"foo"}}}, 1, 2, 3)
    'foo'
    """
    for key in keys:
        if key in obj:
            obj = obj[key]
        else:
            return default
    return obj

