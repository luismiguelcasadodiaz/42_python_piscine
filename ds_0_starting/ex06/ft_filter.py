def ft_filter(filter_func, object):
    """Reproduces behavior of the built-in filter function with generator."""
    for element in object:
        if filter_func is None:
            if element:
                yield element
        else:
            if filter_func(element):
                yield element
