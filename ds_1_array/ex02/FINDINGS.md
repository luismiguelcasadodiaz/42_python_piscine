# Loading Images — Findings

## Images as 3D arrays — `(height, width, channels)`

An image loaded into NumPy is a **3D ndarray**:

```
shape = (height, width, channels)
        (257,   450,   3)
```

The third dimension represents the RGB colour channels — every pixel is
an array of 3 values `[R, G, B]`, each an integer in range 0–255 (`uint8`).

```python
arr[row, col]        # → array([R, G, B], dtype=uint8)
arr[row, col, 0]     # → Red channel value for that pixel
arr[row, col, 1]     # → Green channel value
arr[row, col, 2]     # → Blue channel value
```

This is the bridge between abstract array operations and real image data.

## PIL / Pillow

**PIL** (Python Imaging Library) was created in 1995 but stalled around 2009.
**Pillow** is the community fork — actively maintained, the de facto replacement.

```bash
pip install Pillow    # install as Pillow
```
```python
from PIL import Image  # but import as PIL (namespace kept for compatibility)
```

`Image.open(path)` decodes the binary JPEG format into a Python-usable
`Image` object, which is then converted to a NumPy array.

## `with` context manager for file handling

Opening an image inside a `with` block guarantees the file is closed
even if an exception occurs:

```python
with Image.open(abspath) as im:
    arr = np.array(im, dtype = np.uint8)
```

Without `with`, a crash mid-function could leave the file handle open,
leaking resources. The `with` statement calls `__exit__` automatically.

## `np.array()` vs `np.asarray()`

| | Copies data | Use when |
|-|-------------|----------|
| `np.array(obj)` | always | you want an independent copy |
| `np.asarray(obj)` | only if needed | input may already be an ndarray |

For large images, `np.asarray()` avoids an unnecessary memory copy.
Both return an `ndarray` — the difference is only in memory behaviour.

## `os.path` — systematic path validation

A file path should be validated in order before opening:

```python
abspath = os.path.abspath(path)      # resolve to absolute path
os.path.exists(abspath)              # does it exist?
os.path.isfile(abspath)              # is it a file (not a directory)?
os.access(abspath, os.R_OK)          # does the user have read permission?
_, ext = os.path.splitext(abspath)   # extract extension
ext.lower() in (".jpg", ".jpeg")     # is it a supported format?
```

## `os.path.abspath()` — the right way to resolve paths

An early attempt at manual path resolution with `match/case`:

```python
match path[0]:
    case "/":   return path                          # absolute
    case ".":   return os.path.join(os.getcwd(), path)  # relative
    case _:     return os.path.join(os.getcwd(), path)
```

This fails for edge cases like `../ex01/landscape.jpg` — the manual approach
produces `…/ex02/../ex01/landscape.jpg` instead of the resolved
`…/ex01/landscape.jpg`.

`os.path.abspath()` handles all cases correctly in one call — it resolves
`..`, `.`, and bare filenames against the current working directory:

```python
os.path.abspath("landscape.jpg")         # → /abs/path/ex02/landscape.jpg
os.path.abspath("./landscape.jpg")       # → /abs/path/ex02/landscape.jpg
os.path.abspath("../ex01/landscape.jpg") # → /abs/path/ex01/landscape.jpg
```

**Lesson:** before writing manual path parsing, check if `os.path` already
provides exactly what you need.

## `uint8` dtype — image pixel range

Image pixels are stored as **unsigned 8-bit integers**:

- Range: 0–255
- `dtype = np.uint8`
- 3 channels × 1 byte = 3 bytes per pixel

This is the standard dtype for 8-bit colour images. Operations that
exceed the range will wrap around silently — `255 + 1 = 0` in `uint8`.
Cast to `float32` or `float64` before doing arithmetic on pixel values.



[return](../../README.md)
