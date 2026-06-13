import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a 2D list and print shape before and after."""
    assert isinstance(family, list), "object is not a list"
    n = len(family)
    assert n > 0, "Empty list"
    assert all(
        len(family[i]) == len(family[i + 1])
        for i in range(0, n - 1)
    ), "sizes of List's element do not match"
    assert not isinstance(start, bool) \
        and isinstance(start, int) \
        and abs(start) <= n, \
        "start is not integer or is out of range"
    assert not isinstance(end, bool) \
        and isinstance(end, int) \
        and abs(end) <= n, \
        "end is not integer or is out of range"

    array2D = np.array(family)
    print(f"My shape is : {array2D.shape}")
    newarray2D = array2D[start:end]
    print(f"My new shape is : {newarray2D.shape}")
    return newarray2D.tolist()


def main():
    """Test slice_me with valid and edge-case inputs."""
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, -2, -2))
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
    print(slice_me(family, -1, -2))
    family = [[], [], [], []]
    print(slice_me(family, 1, -2))
    print(slice_me([[], [], [], []], 1, -2))


if __name__ == "__main__":
    main()
