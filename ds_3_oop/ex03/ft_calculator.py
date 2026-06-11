class Calculator:
    def __init__(self, data: list = None):
        """Initialize the calculator with a list of numeric values.

        Args:
            data: A list of numbers. Defaults to None, in which case
                an empty list is created to avoid the mutable default
                argument pitfall.
        """
        if data is None:
            self.data = []
        else:
            self.data = data

    def __add__(self, object) -> None:
        """Add a scalar to each element in the list, in place.

        Args:
            object: The numeric value to add to each element.
        """
        for i in range(len(self.data)):
            self.data[i] += object
        print(self.data)

    def __mul__(self, object) -> None:
        """Multiply each element in the list by a scalar, in place.

        Args:
            object: The numeric value to multiply each element by.
        """
        for i in range(len(self.data)):
            self.data[i] *= object
        print(self.data)

    def __sub__(self, object) -> None:
        """Subtract a scalar from each element in the list, in place.

        Args:
            object: The numeric value to subtract from each element.
        """
        for i in range(len(self.data)):
            self.data[i] -= object
        print(self.data)

    def __truediv__(self, object) -> None:
        """Divide each element in the list by a scalar, in place.

        Args:
            object: The numeric value to divide each element by.

        Raises:
            ZeroDivisionError: If ``object`` is zero.
        """
        if object != 0:
            for i in range(len(self.data)):
                self.data[i] /= float(object)
            print(self.data)
        else:
            raise ZeroDivisionError("Division by zero")
