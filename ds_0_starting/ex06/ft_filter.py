def ft_filter(filter_func, object):
    """Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true."""
    for element in object:
        if filter_func is None:
            if element:
                yield element
        else:
            if filter_func(element):
                yield element
