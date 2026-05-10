# Modules, time, and f-strings — Findings

## Modules and importation

Python comes with 200+ built-in modules (the **standard library** — no `pip` needed).
Third-party libraries live on **PyPI** and are installed with `pip install`.

Key standard library groups:

| Purpose | Modules |
|---------|---------|
| Data & math | `math`, `random`, `statistics`, `collections`, `itertools` |
| Text | `string`, `re`, `textwrap` |
| Files & OS | `os`, `sys`, `pathlib`, `shutil`, `glob` |
| Date & time | `time`, `datetime`, `calendar` |
| I/O & formats | `json`, `csv`, `sqlite3`, `zipfile` |
| Networking | `http`, `urllib`, `socket` |
| Dev tools | `logging`, `unittest`, `argparse`, `typing` |

## Exploring a module with `dir()` and docstrings

```python
import time
data = [x for x in dir(time) if not x.startswith('_')]
for e in data:
    func = getattr(time, e)
    doc = getattr(func, '__doc__', 'No Docstring')
    print(f'--- {e} ---')
    print(doc)
```

`dir(module)` returns all public names. `__doc__` holds the docstring for each member.

## The `time` module — key members

| Member | Description |
|--------|-------------|
| `time.time()` | Seconds since the Unix Epoch (Jan 1, 1970) as float |
| `time.time_ns()` | Same but in nanoseconds as int |
| `time.localtime()` | Convert epoch seconds to a local `struct_time` |
| `time.gmtime()` | Convert epoch seconds to UTC `struct_time` |
| `time.strftime(fmt)` | Format a `struct_time` as a string |
| `time.strptime(s, fmt)` | Parse a string into a `struct_time` |
| `time.monotonic()` | Monotonic clock — never goes backward, good for measuring elapsed time |
| `time.perf_counter()` | High-resolution clock for benchmarking |
| `time.sleep(s)` | Pause execution for `s` seconds |
| `time.struct_time` | Named tuple with fields: tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst |

## f-strings and format codes

An f-string embeds Python expressions inside `{}`, evaluated at runtime:

```python
import time
now = time.time()
print(f"Seconds since Epoch: {now:,.4f}")       # fixed-point, 4 decimals, thousands separator
print(f"Scientific notation: {now:.2e}")         # scientific notation, 2 decimals
```

Common format specifiers (same logic as C `printf`):

| Specifier | Meaning |
|-----------|---------|
| `:.4f` | Float with 4 decimal places |
| `:,.2f` | Float with thousands separator and 2 decimals |
| `:.2e` | Scientific notation |
| `:d` | Integer |
| `:>10` | Right-align in field of width 10 |
| `:<10` | Left-align in field of width 10 |

[return](../../README.md)