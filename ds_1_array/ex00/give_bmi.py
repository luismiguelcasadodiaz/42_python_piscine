import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate BMI values from matching lists of heights and weights."""
    # 1.- convert arguments into numpy arrays
    h = np.array(height)
    w = np.array(weight)

    # 2.- check all what is requiered
    assert w.shape == h.shape, "Lists's lengths must be equal"
    assert w.shape[0] != 0, "Lists cannot be empty"
    assert np.issubdtype(h.dtype, np.number), "height values not numerical"
    assert np.issubdtype(w.dtype, np.number), "weight values not numerical"
    assert np.all(w > 0), "weight has negative or zero values"
    try:
        min_safe = np.finfo(h.dtype).eps
    except ValueError:  # it is not an inexact value
        min_safe = 0
    assert np.all(h > min_safe), "height has negative or too small values"

    # 3.- Calculate bmi
    bmi = w / (h ** 2)
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a boolean array indicating which BMI values exceed the limit."""
    assert isinstance(limit, (int, float)), "Wrong limit's type"
    bmi_array = np.array(bmi)
    assert np.issubdtype(bmi_array.dtype, np.number), "Not numerical values"
    return bmi_array > limit


def main():
    w = [80, 178, 100]
    h = [134, 0, 126.9]
    print(give_bmi(h, w))


if __name__ == "__main__":
    main()
