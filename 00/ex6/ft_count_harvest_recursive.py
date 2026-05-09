def helper_function(days: int):
    if days > 1:
        helper_function(days - 1)
        print("Day ", days)
    else:
        print("Day ", days)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: ") or 0)
    if days:
        helper_function(days)
        print("Harvest time!")
