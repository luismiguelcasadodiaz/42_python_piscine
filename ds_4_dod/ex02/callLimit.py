from typing import Any


def callLimit(limit: int):
    """Create a decorator that limits how many times a function can be called.

    Uses nested closures to track the remaining call count. Once the
    limit is reached, subsequent calls print an error message instead
    of executing the function.

    Args:
        limit: The maximum number of times the decorated function
            can be called.

    Returns:
        A decorator (callLimiter) that wraps a function with call
        counting logic.

    Example:
        >>> @callLimit(3)
        ... def greet(name):
        ...     print(f"Hello, {name}")
        >>> greet("Alice")   # Call 1 — works
        Hello, Alice
        >>> greet("Bob")     # Call 2 — works
        Hello, Bob
        >>> greet("Charlie") # Call 3 — works
        Hello, Charlie
        >>> greet("Dave")    # Call 4 — blocked
        Error: <function greet at 0x...> call too many times
    """
    
    count = limit
    def callLimiter(function):
        """Wrap a function with call-count enforcement.

        Args:
            function: The function to decorate.

        Returns:
            The wrapped function (limit_function) that enforces
            the call limit.
        """

        def limit_function(*args: Any, **kwds: Any):
            """Execute original function if calls remain, else print an error.

            Increments the shared counter on each successful call.
            Once the counter reaches the limit, all further calls are
            blocked with an error message.

            Args:
                *args: Positional arguments forwarded to the
                    original function.
                **kwds: Keyword arguments forwarded to the
                    original function.
            """
            nonlocal count
            if count:
                function(*args, **kwds)
                count -= 1
            else:
                print(f"Error: {function} call too many times")

        return limit_function
    return callLimiter
