import numpy as np


def give_bmi(height: list[int | float], 
             weight: list[int | float]) -> list[int | float]:
    """Calculate BMI values from matching lists of heights and weights."""
    assert len(height) == len(weight), "Lists's lengths mus be equal"
    h = np.array(height)
    h2 = h ** 2
    w = np.array(weight)
    bmi = w / h2
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a boolean array indicating which BMI values exceed the given limit."""
    bmi_array = np.array(bmi)
    return bmi_array > limit

def main():
    w = [80, 90, 100]
    h = [134, 167]
    print (give_bmi(h,w))

    cd 
if __name__ == "__main__":
    main()
