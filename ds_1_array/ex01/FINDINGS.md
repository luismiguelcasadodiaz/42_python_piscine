# 2D Arrays and Slicing — Findings

## 2D arrays — the matrix mental model

A list of lists becomes a 2D NumPy array — a matrix with rows and columns:

```python
family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]
array2D = np.array(family)   # shape (4, 2) — 4 rows, 2 columns
```

The `.shape` attribute returns a tuple `(rows, cols)`.
In data science terms: rows = observations, columns = features.

## `.shape` before and after slicing

Printing shape before and after a slice shows concretely what the operation does:

```
My shape is : (4, 2)
My new shape is : (2, 2)   ← 2 rows selected, columns unchanged
```

Only the row dimension changes — columns are always preserved in a row slice.

## Row-wise slicing of 2D arrays

`array[start:end]` on a 2D array selects **rows**, not individual elements:

```python
array2D[0:2]    # rows 0 and 1
array2D[1:-2]   # row 1 up to (not including) the second-to-last
```

This is the fundamental operation for selecting subsets of observations
from a dataset.

## Negative indices in slices

Negative indices count from the end of the axis:

```python
array[-1]       # last row
array[-2:]      # last two rows
array[1:-2]     # row 1 up to but not including the second-to-last row
```

NumPy **clamps** out-of-range slice indices silently — no IndexError is raised.
`array[0:99]` on a 4-row array simply returns all 4 rows.

## NumPy slice clamping vs Python list behaviour

| Slice | Python list (4 items) | NumPy array (4 rows) |
|-------|-----------------------|----------------------|
| `[0:99]` | returns all 4 items | returns all 4 rows |
| `[5:1]` | returns `[]` | returns empty array |
| `[-4:2]` | works | works |

Because NumPy clamps, validating `start`/`end` ranges in your own function
must be done carefully — overly strict checks reject valid inputs that NumPy
itself would handle gracefully.

## Validating 2D input

Two checks specific to 2D arrays:

**1. Rectangular — all rows same length:**
```python
assert all(
    len(family[i]) == len(family[i + 1])
    for i in range(n - 1)
), "sizes of List's element do not match"
```

**2. Bool guard on integer parameters:**
```python
assert not isinstance(start, bool) and isinstance(start, int)
```
`bool` is a subclass of `int` in Python — `isinstance(True, int)` is `True`.
Without the explicit `not isinstance(start, bool)` check, `True` and `False`
would silently pass as valid integers.

## `.tolist()` — converting back from ndarray to list

The return type is `list`, so the sliced array must be converted back:

```python
return newarray2D.tolist()
```

`ndarray.tolist()` recursively converts all NumPy scalars to native Python
types — `np.float64` becomes `float`, `np.int64` becomes `int`.



[return](../../README.md)
