# Dictionaries — Findings

## Dictionary as a lookup table

The main lesson is architectural: replacing 36 `elif` branches with a single
dictionary lookup. A dict provides **O(1)** access regardless of the number
of entries:

```python
# Without dict — unscalable
if char == 'A':
    return '.-'
elif char == 'B':
    return '-...'
...

# With dict — clean and scalable
NESTED_MORSE[char]
```

Dictionary syntax:
```python
d = {key: value, ...}   # literal
d[key]                  # lookup — raises KeyError if missing
d.get(key, default)     # safe lookup — returns default if missing
key in d                # membership test
```

## Module-level constants

`NESTED_MORSE` is defined at module level in ALL_CAPS — the Python convention
(PEP 8) for constants. This is a **data declaration**, not executable logic,
so it does not violate the "no code in global scope" rule from Chapter VII.

```python
NESTED_MORSE = {
    ' ': '/',
    'A': '.-',
    ...
}
```

## Input normalisation with `str.upper()`

All dictionary keys are uppercase. Rather than duplicating every key in
lowercase, the input is normalised once before lookup:

```python
main(sys.argv[1].upper())
```

This is a common defensive pattern: normalise at the boundary, keep the
data structure simple.

## `all()` with a generator expression

`all()` returns `True` if every element of the iterable is truthy.
It **short-circuits** — stops at the first `False`:

```python
all(c.isalnum() or c.isspace() for c in sys.argv[1])
```

The `for c in ...` without square brackets is a **generator expression** —
lazy, unlike a list comprehension. No list is built in memory; values are
produced one at a time and consumed immediately by `all()`.

| | Evaluated | Memory |
|-|-----------|--------|
| List comprehension `[...]` | all at once | full list |
| Generator expression `(...)` | on demand | one item at a time |

## `print()` with `end` parameter

By default `print()` appends `\n`. The `end` parameter overrides this:

```python
print(NESTED_MORSE[data[i]], ' ', end="")  # no newline, stay on same line
print(NESTED_MORSE[data[n - 1]])           # final item gets the default \n
```

## `main()` with a parameter

Unlike previous exercises, `main(data)` receives a value. `main()` is a
regular function — it can take any arguments. The entry point pattern
does not require a parameterless `main()`:

```python
if __name__ == "__main__":
    ...
    main(sys.argv[1].upper())
```

## `range()` for indexed iteration

```python
for i in range(0, n - 1):
    print(NESTED_MORSE[data[i]], ' ', end="")
```

`range(start, stop)` produces integers from `start` up to but **not**
including `stop`. Used here to process all characters except the last,
which is handled separately to control the final newline.



[return](../../README.md)
