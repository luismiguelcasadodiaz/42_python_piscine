# First Standalone Program — Findings

## String iteration and character classification

Iterating over a string yields one character at a time. `str` class methods
classify each character without any manual comparison:

| Method | Returns `True` when |
|--------|---------------------|
| `c.isupper()` | character is an uppercase letter |
| `c.islower()` | character is a lowercase letter |
| `c.isdigit()` | character is a decimal digit |
| `c.isspace()` | character is whitespace (space, `\t`, `\n`, ...) |
| `c.isalnum()` | character is a letter or digit |
| `c.isprintable()` | character is printable |

Since `bool` is a subclass of `int`, the results can be accumulated directly:

```python
for char in data:
    upp += char.isupper()   # True == 1, False == 0
```

There is no built-in `ispunctuation()`. Punctuation can be derived as:

```python
def is_punctuation(c) -> bool:
    """Returns True if c is a punctuation mark."""
    return c.isprintable() and not c.isalnum() and not c.isspace()
```

## Reading user input: `input()` vs `sys.stdin.read()`

| Method | Strips trailing `\n` | Stops at |
|--------|----------------------|----------|
| `input()` | yes | Enter |
| `sys.stdin.readline()` | no | Enter (waits for `\n`, ctrl+D unreliable mid-line) |
| `sys.stdin.read()` | no | EOF (ctrl+D) |

When the carriage return must be counted as a space, use `sys.stdin.read()`:

```python
print("What is the text to count?")
stats(sys.stdin.read())
```

- Type text + **Enter** → `\n` included → counted as space
- Type text + **ctrl+D** (twice, or once on empty line) → no `\n` → not counted

## The `if __name__ == "__main__"` guard

Every non-trivial Python program should use this pattern:

```python
def main():
    """Entry point."""
    ...

if __name__ == "__main__":
    main()
```

- `__name__` equals `"__main__"` when the file is run directly
- `__name__` equals the module name when the file is imported
- This prevents side effects when the file is used as a module

## Docstrings — PEP 257

All functions must be documented with a `__doc__` string. PEP 257 conventions:

```python
def stats(data: str):
    """
    Count and print upper, lower, punctuation, spaces and digits in data.

    Parameters:
        data (str): The string to make stats from.

    Returns:
        Nothing

    Raises:
        Nothing
    """
```

- One-liners for simple functions, multi-line for complex ones
- Accessible at runtime via `function.__doc__`

## Functions vs procedures

| | Returns a value | Side effects |
|-|-----------------|--------------|
| **Function** | yes | optional |
| **Procedure** | no (`None`) | yes (e.g. `print`) |

In Python both are defined with `def`, but the distinction matters for design.
`is_punctuation` is a function (returns `bool`). `stats` is a procedure (only prints).

## PEP8 and flake8

PEP8 is the official Python style guide. **flake8** is the linter that enforces it:

```bash
pip install flake8       # first pip install from PyPI
flake8 building.py       # check the file
```

Key rules: 2 blank lines between top-level definitions, spaces around operators,
max line length 79 characters, no trailing whitespace.

At 42, `flake8` is aliased as `norminette`:

```bash
alias norminette=flake8
```



[return](../../README.md)
