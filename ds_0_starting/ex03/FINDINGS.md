# Scalar Types and Null-like Values — Findings

## Python has no single NULL

Unlike C, Python has several scalar values that act as "null-like" or falsy,
each with a distinct type:

| Name | Value | Type |
|------|-------|------|
| `Nothing` | `None` | `NoneType` — Python's true null |
| `Garlic` | `float("NaN")` | `float` — undefined numeric result |
| `Zero` | `0` | `int` |
| `Empty` | `""` | `str` |
| `Fake` | `False` | `bool` |

## NaN — Not a Number

`NaN` comes from the **IEEE 754** floating-point standard, followed by every
language (C, Java, JavaScript, Rust, Python). It represents the result of an
undefined or nonsensical calculation:

```python
float("inf") - float("inf")   # nan
0 * float("inf")               # nan
```

These two `nan` values come from completely different operations — they do not
represent the same thing. Comparing them as equal would be misleading.

> "I got an error" and "you got an error" does not mean you got the **same** error.

This is why the standard defines that `nan` is not equal to anything,
**including itself**:

```python
nan = float("nan")
nan == nan   # False
nan != nan   # True
```

This behaviour is the only case in Python where `x != x` is `True`.

## `False` and `0` are the same

`bool` is a subclass of `int` in Python. `False` and `0` are identical in value:

```python
False == 0     # True
True  == 1     # True
type(False)    # <class 'bool'>
type(0)        # <class 'int'>
```

They share the same value but have different types — type introspection
(`__class__.__name__`) is needed to tell them apart.

## Return convention

The function returns `0` on success (known type) and `1` on error (unknown type),
mirroring the Unix exit code convention.



[return](../../README.md)
