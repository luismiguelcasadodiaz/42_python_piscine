# Rotating Images — Findings

## `np.zeros()` defaults to `float64`

`np.zeros()` creates an ndarray of **floats** by default:

```python
arr = np.zeros((h, w))          # dtype=float64
arr = np.zeros((h, w), dtype=np.uint8)  # correct for pixel data
```

`Image.fromarray()` only accepts specific dtypes (`uint8`, `uint32`,
`float32` in specific modes). Passing a `float64` array raises a `TypeError`.
Always specify `dtype=np.uint8` when allocating an output buffer for pixel
data.

---

## 90° counter-clockwise rotation — index remapping

A 90° CCW rotation transforms axes as follows:

- The original **x-axis becomes the rotated y-axis**
- The original **first row becomes the rotated first column**
- The original **lower x becomes the rotated higher y**

Concretely, given a source array of shape `(H, W)`:

- Output shape is `(W, H)` — height and width swap
- The mapping is: `rotated[y, x] = original[x, W - 1 - y]`

```python
arr_rotated = np.zeros((arr_cropped.shape[1], arr_cropped.shape[0]),
                       dtype=np.uint8)
for y in range(arr_rotated.shape[0]):
    for x in range(arr_rotated.shape[1]):
        arr_rotated[y, x] = arr_cropped[x, arr_cropped.shape[1] - y - 1]
```

Breaking down `rotated[y, x] = original[x, W-1-y]`:

| rotated axis | comes from original axis | transformation |
|---|---|---|
| row `y` | column | `W-1-y` reverses the original column order |
| col `x` | row | `x` maps directly to original row |

The nested loops make the index remapping explicit — the same result can be
achieved in one line with `np.rot90(arr, k=1)`, but writing it manually is the
point of the exercise.

---

## Shape change on rotation

Before rotation, `zoom_42` returns a grayscale `"L"` PIL image. Converting to
a NumPy array gives a **2D** array `(H, W)`. After a 90° rotation the shape
becomes `(W, H)`:

```python
arr_cropped.shape   # (H, W)  — portrait or landscape
arr_rotated.shape   # (W, H)  — axes swapped
```

This shape change must be reflected in the output buffer allocation —
`np.zeros` must receive `(W, H)`, not `(H, W)`.

---

## `arr[y][x]` vs `arr[y, x]`

Both index the same element, but they differ internally:

- `arr[y][x]` — two separate indexing steps; the first creates an intermediate
  1D array (a view), then the second indexes into it
- `arr[y, x]` — single multi-dimensional index; no intermediate object

`arr[y, x]` is the idiomatic NumPy form and avoids the unnecessary
intermediate view.



[return](../../README.md)
