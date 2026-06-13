class calculator:
    """A static vector calculator for basic operations on numeric lists.

    Provides dot product, element-wise addition, and element-wise
    subtraction between two vectors represented as lists of floats.
    All methods are static and print their results to stdout.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Compute and print the dot product of two vectors.

        Calculates the sum of element-wise products of V1 and V2.

        Args:
            V1: The first vector as a list of floats.
            V2: The second vector as a list of floats.

        Raises:
            AssertionError: If V1 and V2 have different lengths.
        """
        size = len(V1)
        assert size == len(V2), "vector with different length"
        result = 0
        for i in range(size):
            result += V1[i] * V2[i]
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Compute and print the element-wise addition of two vectors.

        Args:
            V1: The first vector as a list of floats.
            V2: The second vector as a list of floats.

        Raises:
            AssertionError: If V1 and V2 have different lengths.
        """
        size = len(V1)
        assert size == len(V2), "vector with different length"
        result = []
        for i in range(size):
            result.append(float(V1[i] + V2[i]))
        print(f"Add Vector is: {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Compute and print the element-wise subtraction of two vectors.

        Args:
            V1: The first vector as a list of floats.
            V2: The second vector as a list of floats.

        Raises:
            AssertionError: If V1 and V2 have different lengths.

        Note:
            Bug — the operation uses ``+`` instead of ``-``, making
            this identical to ``add_vec``. The line should read:
            ``result.append(float(V1[i] - V2[i]))``
        """
        size = len(V1)
        assert size == len(V2), "vector with different length"
        result = []
        for i in range(size):
            result.append(float(V1[i] - V2[i]))
        print(f"Sous Vector is: {result}")
