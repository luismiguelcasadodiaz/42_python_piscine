# NumPy Arrays, Type Hierarchy, and pytest — Findings

## `np.array()` — converting lists to arrays

`np.array(list)` transforms a Python list into a NumPy `ndarray`.
All elements are coerced to a **single shared dtype**:

```python
np.array([1, 2.5, "hello"])   # → array(['1', '2.5', 'hello'], dtype='<U32')
```

If a string is present, every element becomes a string. NumPy always
picks the dtype that can represent all values — no exceptions, no errors.
This is why dtype validation after conversion is essential.

## `isinstance()` vs `type()` — always prefer `isinstance`

`type(x) == int` is **too strict** — it breaks two major Python features:

**1. Booleans are integers:**
```python
type(True) == int    # False  ← breaks
isinstance(True, int)  # True  ← correct
```

**2. NumPy scalars are not Python scalars:**
```python
x = np.int64(5)
type(x) == int        # False  ← breaks
isinstance(x, int)    # True   ← correct (np.int64 inherits from int)
```

`isinstance(x, T)` checks the full inheritance chain — it accepts the class
and all its subclasses. Use it whenever accepting a type family, not an exact type.

## The NumPy type hierarchy

NumPy organises dtypes into a family tree:

```
np.generic
└── np.number
    ├── np.integer
    │   ├── np.int8, np.int16, np.int32, np.int64
    │   └── np.uint8, np.uint16, ...
    └── np.inexact
        ├── np.float16, np.float32, np.float64
        └── np.complex64, np.complex128
```

## `np.issubdtype()` — checking dtype families

Instead of asking "is this exactly float64?", ask "is this any floating-point?":

```python
np.issubdtype(arr.dtype, np.number)    # any numeric type
np.issubdtype(arr.dtype, np.integer)   # any integer
np.issubdtype(arr.dtype, np.inexact)   # any float or complex
```

Combined with `np.array()` conversion, this is the idiomatic way to validate
numeric input: convert first, then check dtype — one pass, no element loops.

## `np.all()` — validate entire arrays at once

```python
np.all(w > 0)    # True if every element of w is positive
np.all(h > 0)    # True if every element of h is positive
```

Vectorised — no Python loop needed. Works on any boolean array expression.

## `np.finfo()` — floating-point machine limits

`np.finfo(dtype)` returns the limits of a floating-point type:

```python
np.finfo(np.float64).eps        # machine epsilon ≈ 2.22e-16
np.finfo(np.float32).tiny       # smallest normal float ≈ 1.18e-38
np.finfo(np.float32).max        # largest representable float ≈ 3.4e+38
```

Useful for guarding against division by near-zero values that would silently
produce `inf` instead of raising an error.
`np.iinfo(dtype)` is the equivalent for integer types.

## Vectorised BMI calculation

Converting to arrays allows the formula to be expressed as a single line
with no loop — this is the NumPy way:

```python
bmi = w / (h ** 2)    # operates on every element simultaneously
```

This is faster than a Python loop for large datasets and more readable.

## `pytest` — structured testing

`pytest` discovers and runs test functions automatically.
Run a specific test file with:
```bash
pytest -v ./test_bmi_calculator.py
```

Two kinds of tests are needed:

**Happy path — what should work:**
```python
def test_give_bmi_integers():
    """Test standard BMI calculation with integer inputs."""
    heights = [2, 2]
    weights = [80, 100]
    result = give_bmi(heights, weights)
    assert np.allclose(result, [20.0, 25.0])
```

**Error path — what should fail:**
```python
def test_give_bmi_mismatched_lengths():
    """Test that mismatched list lengths trigger an AssertionError."""
    with pytest.raises(AssertionError) as exc_info:
        give_bmi([1.80, 1.75], [80])
    assert "Lists's lengths must be equal" in str(exc_info.value)
```

## `np.allclose()` — floating-point comparison

Never use `==` to compare floats — rounding errors make results differ by tiny amounts.
`np.allclose(a, b)` returns `True` if all elements are within a tolerance:

```python
np.allclose([20.000000000001], [20.0])   # True
[20.000000000001] == [20.0]              # False
```

Default tolerances: `rtol=1e-5` (relative), `atol=1e-8` (absolute).



[return](../../README.md)
