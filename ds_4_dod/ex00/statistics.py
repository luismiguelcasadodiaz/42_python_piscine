from typing import Any


def ft_mean(*args: Any) -> float:
    n = len(args)
    sum = 0
    for value in args:
        sum += value
    return sum / n


def ft_median(args: Any) -> float:
    sorted_values = sorted(args)
    n = len(sorted_values)
    if n % 2 == 1:
        return sorted_values[n // 2]
    else:
        return (sorted_values[n // 2 - 1] + sorted_values[n // 2]) / 2


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    assert all(isinstance(valor, int) or
               isinstance(valor, float) for valor in args)
    print(f"mean: {ft_mean(args)}")
    print(f"median: {ft_median(args)}")
