# CLI Input, Assert, and Exceptions — Findings

## `sys` module — key members used

| Member | Description |
|--------|-------------|
| `sys.argv` | List of CLI arguments; `sys.argv[0]` is the script name, `sys.argv[1]` onward are user inputs — always `str` |
| `sys.exit(code)` | Exits the program immediately; `0` means success, non-zero means error |
| `sys.tracebacklimit = 0` | Suppresses the traceback, printing only the exception type and message |
| `del sys.tracebacklimit` | Restores full verbosity — `del` removes a name from the namespace |

## `assert` — defensive validation

`assert <condition>, "message"` raises `AssertionError` if the condition is `False`:

```python
assert len(sys.argv) == 2, "more than one argument is provided"
```

It is used here to enforce preconditions on input before proceeding.

## EAFP — Easier to Ask Forgiveness than Permission

Python favors **EAFP** over checking types/values upfront (LBYL — Look Before You Leap).
Instead of testing whether a conversion is possible, just try it and handle the error:

```python
try:
    n = int(sys.argv[1])
except ValueError:
    raise AssertionError("argument is not an integer")
```

## Exception types and chaining

Common general-purpose exceptions:

| Exception | When raised |
|-----------|-------------|
| `AssertionError` | `assert` statement fails |
| `ValueError` | Right type, wrong value (e.g. `int("Hi")`) |
| `TypeError` | Wrong type entirely |
| `IndexError` | Sequence index out of range |
| `KeyError` | Dict key not found |

**Exception chaining** with `raise ... from ...` lets you link a new exception
to the original cause, preserving context:

```python
except ValueError as e:
    raise AssertionError("argument is not an integer") from e
```

Using a bare `except:` is discouraged — it catches everything including
`KeyboardInterrupt` and `SystemExit`. Always catch the most specific exception possible.

## Modulo `%` — even/odd

```python
n % 2 == 0   # True → even
n % 2 != 0   # True → odd
```

Works correctly for negative numbers too (`-5 % 2 == 1` in Python).

## Execution flow

```
no args       → silent exit (sys.exit(0))
> 1 arg       → AssertionError: more than one argument is provided
arg not int   → AssertionError: argument is not an integer
valid int     → "I'm Even." or "I'm Odd."
```



[return](../../README.md)
