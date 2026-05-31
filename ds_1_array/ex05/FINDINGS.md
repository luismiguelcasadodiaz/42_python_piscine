# Colour Filters — Findings

## Assignment does not copy a NumPy array

Assigning one ndarray to another variable creates a **view** — both names
point to the same data. Modifying one modifies the other:

```python
red = array          # NOT a copy — same memory
red[:, :, 1] = 0    # also zeroes array's green channel!
```

To get an independent copy, call `.copy()` explicitly:

```python
red = array.copy()   # independent buffer
red[:, :, 1] = 0    # array is unaffected
```

This matters whenever you want to modify a channel in isolation without
corrupting the original image passed to the function.

---

## Channel isolation — targeting one axis of a 3D array

An RGB image is a 3D array `(H, W, 3)`. The third axis is the channel:
index `0` = R, `1` = G, `2` = B.

To isolate red, zero the other two channels in-place on the copy:

```python
red[:, :, 1] = 0   # zero green for every pixel
red[:, :, 2] = 0   # zero blue  for every pixel
```

`arr[:, :, n]` selects **all rows, all columns, channel n** — a 2D slice
across the whole spatial extent of the image. This is the canonical NumPy
pattern for per-channel manipulation.

---

## Colour inversion — scalar broadcast

Inverting pixel values means flipping the 0–255 range: black becomes white,
white becomes black, and every intermediate tone is reflected.

```python
inverted = 255 - array
```

NumPy **broadcasts** the scalar `255` across every element of the 3D array at
once — no loop required. Because `array` is `uint8`, the result is guaranteed
to stay in range (`255 - x` for `x` in 0–255 is always 0–255). A new array is
created; the original is not modified.

---

## Grayscale via dot product — luminance the hard way

`convert("L")` (PIL) and `np.mean(..., axis=2)` both produce grayscale, but
neither uses perceptually correct weights. The ITU-R BT.601 luminance formula
is:

```
L = 0.299 × R + 0.587 × G + 0.114 × B
```

In NumPy this is a **dot product** between each pixel's RGB vector and the
weight vector:

```python
grey = np.dot(array[:, :, :3], [0.299, 0.587, 0.114])
```

`array[:, :, :3]` has shape `(H, W, 3)`; the weight vector has shape `(3,)`.
NumPy contracts the last axis of the array against the weight vector, producing
a `(H, W)` float64 array.

Because the weights are floats, the output is `float64` — outside the valid
`uint8` pixel range representation. Cast back explicitly:

```python
grey = np.dot(array[:, :, :3], [0.299, 0.587, 0.114]).astype(np.uint8)
```

`.astype()` truncates the float to the nearest integer and wraps into 0–255.

---

## matplotlib subplots — `plt.subplots(rows, cols)`

`plt.subplots(3, 2)` returns a `Figure` and a 2D array of `Axes` objects with
shape `(3, 2)`. Each subplot is addressed like a NumPy array element:

```python
fig, axes = plt.subplots(3, 2, figsize=(8, 12))
axes[0, 0].imshow(array)
axes[0, 0].set_title("Original")
```

Useful helpers for a grid of image subplots:

```python
for ax in axes.flat:   # iterate all axes as a flat sequence
    ax.axis('off')     # hide tick marks and axis lines

plt.tight_layout()     # remove excess whitespace between subplots
plt.show()
```

`axes.flat` returns a flat iterator over the 2D axes array — avoids nested
loops when applying the same setting to every subplot.

---

## `cmap='gray'` for 2D arrays in matplotlib

Passing a 2D NumPy array to `plt.imshow()` without a colormap applies
**viridis** by default — the grayscale data appears in purple/yellow tones.
Always pass the array directly with `cmap='gray'`:

```python
plt.imshow(grey, cmap='gray')   # correct
plt.imshow(Image.fromarray(grey))  # wrong — viridis applied
```

Wrapping in `Image.fromarray()` before passing to matplotlib is also
unnecessary: matplotlib accepts NumPy arrays directly.



[return](../../README.md)
