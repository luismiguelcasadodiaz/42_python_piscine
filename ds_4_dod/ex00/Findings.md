# ds_4_dod — Exercise 00: Findings

## Learning aims

### Variadic functions — `*args` and `**kwargs`

A variadic function accepts an unknown number of arguments at call time.

`*args` collects any number of positional arguments into a **tuple**:

```python
def greet(*args):
    for name in args:
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")
```

`**kwargs` collects any number of keyword arguments into a **dictionary**:

```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="Paris")
```

Combined — as in `ft_statistics`:

```python
def ft_statistics(*args: Any, **kwargs: Any) -> None:
    print("Positional args:", args)   # tuple
    print("Keyword   args:", kwargs)  # dict

ft_statistics(1, 2, 3, op="mean", round=2)
# Positional args: (1, 2, 3)
# Keyword   args: {'op': 'mean', 'round': 2}
```

**Argument order rule** — parameters must follow this strict order:

| # | Type | Example |
|---|------|---------|
| 1 | Regular positional | `x, y` |
| 2 | Variadic positional | `*args` |
| 3 | Keyword-only (after `*`) | `mode="fast"` |
| 4 | Variadic keyword | `**kwargs` |

`*` and `**` also work at the **call site** to unpack collections:

```python
nums = [1, 2, 3]
add(*nums)          # same as add(1, 2, 3)

opts = {"a": 1, "b": 2, "c": 3}
add(**opts)         # same as add(a=1, b=2, c=3)
```

### Dispatcher pattern — functions as first-class objects

A dispatcher is a dictionary that maps string names to function references
(not calls — no parentheses). It replaces a long `if/elif` chain with a clean
lookup:

```python
dispatcher = {"mean": ft_mean,
              "median": ft_median,
              "quartile": ft_quartile,
              "std": ft_std,
              "var": ft_variance}

for k, v in kwargs.items():
    if v in dispatcher:
        print(f"{v} : {dispatcher[v](sorted_values, n)}")
    else:
        print("ERROR")
```

`dispatcher[v]` retrieves the function object; `(sorted_values, n)` calls it
immediately. When `v = "mean"`:

```
dispatcher["mean"](sorted_values, n)  →  ft_mean(sorted_values, n)
```

The keys in `kwargs` (`"toto"`, `"tutu"`) are ignored entirely — only the
*values* (`"mean"`, `"median"`) drive the dispatch. This is the key design
insight: `**kwargs` is used not as named configuration but as an ordered list
of operation requests.

This works because **functions are first-class objects** in Python — they can
be stored in variables, placed in dictionaries, and called later.

### `sorted()` on tuples

`*args` arrives as a tuple, which is immutable and cannot be sorted in place.
`sorted()` accepts any iterable (tuple, list, set) and always returns a **new
list** — no conversion needed before calling it.

### Statistical formulas implemented from scratch

| Statistic | Formula |
|-----------|---------|
| Mean | `sum(data) / n` |
| Median | middle element (odd n), average of two middle elements (even n) |
| Quartile | Q1 = 25th percentile, Q3 = 75th percentile via linear interpolation |
| Variance | mean of squared deviations from the mean |
| Std dev | square root of variance |

**Percentile with linear interpolation** — when the index falls between two
data points, interpolate:

```python
index = percentile * (n - 1)
if index % 1 == 0:
    return float(data[int(index)])   # exact hit — cast to float for consistency
else:
    idx = int(index)
    return data[idx] + (data[idx + 1] - data[idx]) * (index % 1)
```

Casting to `float` on the exact-hit branch ensures the output type is always
consistent, regardless of whether the input data contains integers or floats.

---

## Notes on the `typing` module

Type hints are **not enforced at runtime** — Python ignores them during
execution. They exist for:
- Your editor (autocomplete, inline warnings)
- Type checkers like `mypy` or `pyright`
- Code readability

| Type | Meaning |
|------|---------|
| `Any` | any type, disables type checking |
| `Union[int, str]` | int or str |
| `Optional[int]` | int or None |
| `List[int]` | list of ints |
| `Dict[str, int]` | dict with str keys and int values |
| `Callable` | a function |

**Modern syntax (Python 3.10+)** — built-in types can be used directly,
without importing from `typing`:

```python
def foo(x: int | str): ...          # Union
def foo(x: int | None): ...         # Optional
def foo(x: list[int]): ...          # List
def foo(x: dict[str, int]): ...     # Dict
```

---

## Notes on module docstrings

A module docstring is the first string literal at the top of a file, before
any code. Python stores it in `__doc__` — accessible the same way as class and
function docstrings:

```python
import statistics
print(statistics.__doc__)   # prints the module-level docstring
help(statistics)            # full rendered help
print(__doc__)              # from within the module itself
```

Packages can have module docstrings too, by placing one at the top of
`__init__.py`.

[return](../../README.md)
