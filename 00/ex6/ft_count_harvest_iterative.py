def ft_count_harvest_iterative():
    days = int(input("Days until harvest: ") or 0)
    if days:
        for i in range(1, days + 1):
            print("Day ", i)
        print("Harvest time!")
