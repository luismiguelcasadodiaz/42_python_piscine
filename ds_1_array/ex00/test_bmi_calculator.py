import pytest
import numpy as np
from give_bmi import give_bmi  # Assuming your function is in bmi_calculator.py

# =====================================================================
# HAPPY PATHS (Tests where everything should work)
# =====================================================================


def test_give_bmi_integers():
    """Test standard BMI calculation with integer inputs."""
    # Metric formula: weight (kg) / height (m)^2
    # Height 2m, Weight 80kg -> 80 / 4 = 20.0
    heights = [2, 2]
    weights = [80, 100]

    expected = [20.0, 25.0]
    result = give_bmi(heights, weights)

    # Using np.allclose because floating-point
    # math can have tiny rounding variances
    assert np.allclose(result, expected)


def test_give_bmi_numpy_numbers():
    """Test standard BMI calculation with integer inputs."""
    # Metric formula: weight (kg) / height (m)^2
    # Height 2m, Weight 80kg -> 80 / 4 = 20.0
    heights = [np.int32(2), 2]
    weights = [80, np.float64(100.0)]

    expected = [20.0, 25.0]
    result = give_bmi(heights, weights)

    # Using np.allclose because floating-point
    # math can have tiny rounding variances
    assert np.allclose(result, expected)


def test_give_bmi_booleans():
    """Test standard BMI calculation with boolean inputs."""
    # Metric formula: weight (kg) / height (m)^2
    # Height 2m, Weight 80kg -> 80 / 4 = 20.0
    heights = [2, True]
    weights = [80, True]

    expected = [20.0, 1]
    result = give_bmi(heights, weights)

    # Using np.allclose because floating-point
    # math can have tiny rounding variances
    assert np.allclose(result, expected)


def test_give_bmi_floats():
    """Test BMI calculation with floating-point numbers."""
    heights = [1.75]
    weights = [70.0]

    # 70 / (1.75^2) = 70 / 3.0625 = 22.8571...
    expected = [22.857142857142858]
    result = give_bmi(heights, weights)

    assert np.allclose(result, expected)


# =====================================================================
# EDGE CASES & ERROR HANDLING (Testing your assertions)
# =====================================================================

def test_give_bmi_mismatched_lengths():
    """Test that mismatched list lengths trigger an AssertionError."""
    heights = [1.80, 1.75]
    weights = [80]  # Missing one weight

    with pytest.raises(AssertionError) as exc_info:
        give_bmi(heights, weights)

    assert "Lists's lengths must be equal" in str(exc_info.value)


def test_give_bmi_eps():
    """Test that mismatched list lengths trigger an AssertionError."""
    heights = [1.80, np.finfo(np.float64).eps]
    weights = [80, 100]  # Missing one weight

    with pytest.raises(AssertionError) as exc_info:
        give_bmi(heights, weights)

    assert "height has negative or too small values" in str(exc_info.value)


def test_give_bmi_empty_lists():
    """Test that mismatched list lengths trigger an AssertionError."""
    heights = []
    weights = []  # Missing one weight

    with pytest.raises(AssertionError) as exc_info:
        give_bmi(heights, weights)

    assert "Lists cannot be empty" in str(exc_info.value)


def test_give_bmi_non_numerical_height():
    """Test that string values in height trigger an AssertionError."""
    heights = [1.80, "one-eighty"]
    weights = [80, 75]

    with pytest.raises(AssertionError) as exc_info:
        give_bmi(heights, weights)

    assert "height values not numerical" in str(exc_info.value)


def test_give_bmi_non_numerical_weight():
    """Test that string values in weight trigger an AssertionError."""
    heights = [1.80, 1.94]
    weights = [80, "one-eighty"]

    with pytest.raises(AssertionError) as exc_info:
        give_bmi(heights, weights)

    assert "weight values not numerical" in str(exc_info.value)


def test_give_bmi_zero_height():
    """Test a height of zero triggers the specific zero-value assertion."""
    heights = [1.80, 0, 1.70]
    weights = [80, 70, 60]

    with pytest.raises(AssertionError) as exc_info:
        give_bmi(heights, weights)

    assert "height has negative or too small values" in str(exc_info.value)
