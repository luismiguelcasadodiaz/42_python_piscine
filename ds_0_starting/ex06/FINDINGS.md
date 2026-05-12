# Iterators, List Comprehensions, Lambda, and filter() — Findings

## Iterators and lazy evaluation

An **iterator** is an object that produces values one at a time on demand,
without building the full result in memory. `filter()` returns an iterator:

```python
filter(func, iterable)   # returns an iterator, NOT a list
list(filter(func, iterable))  # materialise it into a list
```

This is **lazy evaluation**: values are computed only when requested.
Wrapping with `list()` forces full evaluation.

## List comprehensions

A compact way to build a list by iterating and optionally filtering:

```python
[expression for item in iterable if condition]
```

Example — keep only clean characters:
```python
cleanstring = "".join([c for c in text if goodchar(c)])
```

List comprehensions are preferred over `map()`/`filter()` for readability
when the logic is simple.

## Lambda functions

Anonymous, single-expression functions defined inline:

```python
lambda x: len(x) > n   # equivalent to: def f(x): return len(x) > n
```

Used when a short function is needed as an argument and a named `def` would
add noise. Common with `filter()`, `map()`, `sorted()`.

## `filter()` — built-in and reimplementation

`filter(function, iterable)` keeps elements for which `function` returns `True`.

Reimplementing it with a list comprehension:
```python
def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object  ..."""
    return [x for x in iterable if function(x)]
```

**Special case: `filter(None, iterable)`** — passing `None` filters out all
falsy values (`""`, `0`, `None`, `False`, `[]`):
```python
list(filter(None, [1, 0, "hi", "", None, False, []]))  # [1, 'hi']
```

## `str.split()` and `str.join()`

`split()` without arguments splits on any whitespace and discards empty strings:
```python
"Hello   World".split()       # ['Hello', 'World']
"Hello   World".split(" ")    # ['Hello', '', '', 'World']  ← keeps empties
```

`join()` assembles a list of strings into one:
```python
"".join(['H', 'e', 'l', 'l', 'o'])   # 'Hello'
" ".join(['Hello', 'World'])          # 'Hello World'
```

## Argument type validation

Both argument count and type must be validated:
```python
assert len(sys.argv) == 3, "the arguments are bad"
assert sys.argv[2].lstrip('-').isdigit(), "the arguments are bad"
```

`sys.argv` items are always `str` — `int(sys.argv[2])` raises `ValueError`
if not a valid integer, which must be caught and turned into an `AssertionError`.

## String encoding: `encode()` / `decode('unicode_escape')`

CLI arguments arrive as raw strings. To interpret escape sequences like `\n`
or `\t` passed on the command line:
```python
text = sys.argv[1].encode().decode('unicode_escape')
```
`encode()` converts to bytes, `decode('unicode_escape')` interprets the
escape sequences, yielding the intended characters.

## Cross-module import

Code from another exercise can be reused by extending `sys.path`:
```python
sys.path.append("../ex05")
from building import is_punctuation
```

This is the manual equivalent of installing a local package — useful during
development but fragile in production (path is relative).

## Reimplementing built-ins

Part 1 asks you to recode `filter()` and match its `__doc__` string exactly.
The purpose: understand what the built-in does internally before relying on it.
This is a recurring 42 pattern — recode before you use.



[return](../../README.md)
