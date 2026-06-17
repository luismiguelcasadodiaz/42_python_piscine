"""Descriptive statistics module.

Provides functions for computing common statistical measures — mean,
median, quartiles, variance, standard deviation, and arbitrary
percentiles — on numeric datasets. Includes a dispatcher function
that accepts data as positional arguments and selects operations
via keyword arguments.
"""
from typing import Any


def ft_percentile(percentile: float, data: Any, n: int) -> float:
    """Compute a percentile value using linear interpolation.

    If the computed index falls exactly on a data point, that value is
    returned. Otherwise, linearly interpolates between the two nearest
    data points.

    Args:
        percentile: A float between 0 and 1 representing the desired
            percentile (e.g., 0.25 for the 25th percentile).
        data: A sorted sequence of numeric values.
        n: The number of elements in data.

    Returns:
        The interpolated value at the given percentile.
    """
    index = percentile * (n - 1)
    if index % 1 == 0:
        return float(data[int(index)])
    else:
        idx = int(index)
        a = data[idx]
        b = data[idx + 1]
        diff = b - a
        return a + diff * (index % 1)


def ft_quartile(data: Any, n: int) -> list:
    """Compute the first and third quartiles (Q1 and Q3).

    Args:
        data: A sorted sequence of numeric values.
        n: The number of elements in data.

    Returns:
        A list of two floats: [Q1, Q3].
    """
    return [ft_percentile(0.25, data, n), ft_percentile(0.75, data, n)]


def ft_mean(data: Any, n: int) -> float:
    """Compute the arithmetic mean.

    Args:
        data: A sequence of numeric values.
        n: The number of elements in data.

    Returns:
        The arithmetic mean as a float.
    """
    return sum(data) / n


def ft_median(data: Any, n: int) -> float:
    """Compute the median of a sorted dataset.

    For odd-length data, returns the middle element. For even-length
    data, returns the average of the two middle elements.

    Args:
        data: A sorted sequence of numeric values.
        n: The number of elements in data.

    Returns:
        The median value as a float.
    """
    if n % 2 == 1:
        return data[n // 2]
    else:
        return (data[(n // 2) - 1] + data[n // 2]) / 2


def ft_variance(data: Any, n: int) -> float:
    """Compute the population variance.

    Calculates the average of the squared deviations from the mean.

    Args:
        data: A sequence of numeric values.
        n: The number of elements in data.

    Returns:
        The population variance as a float.
    """
    mean = ft_mean(data, n)
    v_minus_mean = [x - mean for x in data]
    squared_minus_mean = [x * x for x in v_minus_mean]
    return (ft_mean(squared_minus_mean, n))


def ft_std(data: Any, n: int) -> float:
    """Compute the population standard deviation.

    Returns the square root of the population variance.

    Args:
        data: A sequence of numeric values.
        n: The number of elements in data.

    Returns:
        The population standard deviation as a float.
    """
    return ft_variance(data, n) ** (1/2)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Compute and print selected statistics on a numeric dataset.

    Accepts numeric values as positional arguments and operation names
    as keyword argument values. Sorts the data, then dispatches each
    requested operation via an internal lookup table.

    Valid operation names: "mean", "median", "quartile", "std", "var".

    Args:
        *args: Numeric values (int or float) forming the dataset.
        **kwargs: Keyword arguments whose values specify which
            statistics to compute. The keys are ignored; only the
            values are used for dispatch.

    Raises:
        AssertionError: If any positional argument is not an int
            or float.

    Note:
        Prints "ERROR" and returns early if no data is provided,
        or prints "ERROR" for any unrecognized operation name.
    """
    assert all(isinstance(valor, int) or
               isinstance(valor, float) for valor in args), \
        "Not all values are numbers"

    n = len(args)
    if n == 0:
        print("ERROR")
        return
    dispatcher = {"mean": ft_mean,
                  "median": ft_median,
                  "quartile": ft_quartile,
                  "std": ft_std,
                  "var": ft_variance}
    sorted_values = sorted(args)
    for k, v in kwargs.items():
        if v in dispatcher:
            print(f"{v} : {dispatcher[v](sorted_values, n)}")
        else:
            print("ERROR")


def main():
    """Run example statistics computations to demonstrate ft_statistics."""
    ft_statistics(1, 42, 360, 11, 64,
                  toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
