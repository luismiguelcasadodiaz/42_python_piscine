"""Closure-based function accumulator.

Demonstrates closures and higher-order functions by repeatedly
applying a mathematical operation to an accumulated value. Each
call to the returned inner function applies the operation to the
previous result.
"""


def square(x: int | float) -> int | float:
    """Return the square of x.

    Args:
        x: A numeric value.

    Returns:
        x raised to the power of 2.
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return x raised to the power of itself.

    Args:
        x: A numeric value.

    Returns:
        x raised to the power of x.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """Create a closure that repeatedly applies a function to a value.

    Returns an inner function that, on each call, applies ``function``
    to the accumulated result and returns the new value. The state
    persists between calls via the ``nonlocal`` keyword.

    Args:
        x: The initial numeric value.
        function: A callable that takes a single numeric argument and
            returns a numeric value (e.g., ``square``, ``pow``).

    Returns:
        A closure (inner function) that applies ``function`` to the
        accumulated value on each call.

    Example:
        >>> counter = outer(3, square)
        >>> counter()   # square(3) = 9
        9
        >>> counter()   # square(9) = 81
        81
        >>> counter()   # square(81) = 6561
        6561
    """
    count = x

    def inner() -> float:
        """Apply the captured function to the accumulated value.

        Uses ``nonlocal`` to read and update ``count`` from the
        enclosing ``outer`` scope.

        Returns:
            The new accumulated value after applying the function.
        """
        nonlocal count
        count = function(count)
        return count

    return inner


def main():
    """Demonstrate the closure by squaring 3 three times in sequence."""
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())


if __name__ == "__main__":
    main()
