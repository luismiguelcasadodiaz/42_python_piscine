# Type Introspection — Findings

## Type introspection with `__class__.__name__`

Since no built-in functions are allowed, the type of an object is queried directly
from the object itself:

```python
object.__class__.__name__   # returns e.g. 'list', 'str', 'int', ...
```

This is introspection: asking the object at runtime which class it belongs to.
It works because every Python object carries a reference to its class via `__class__`.

## Modules and imports

The function lives in `find_ft_type.py` and is imported by the tester:

```python
from find_ft_type import all_thing_is_obj
```

This is the Python equivalent of a C `#include`: the file acts as a module,
and only the named symbol is brought into scope.

## if / elif / else and the `in` operator

Combining `in` with a predefined list keeps the branching clean:

```python
known_classes = ['list', 'tuple', 'set', 'dict']

def all_thing_is_obj(object: any) -> int:
    object_class = object.__class__.__name__
    if object_class in known_classes:
        print(f"{object_class.capitalize()} : <class '{object_class}'>")
    elif object_class == 'str':
        print(f"{object} is in the kitchen : <class 'str'>")
    else:
        print("Type not found")
    return 42
```

Instead of chaining `object_class == 'list' or object_class == 'tuple' or ...`,
a single `in` test against a list covers all known container types at once.

## `str.capitalize()`

`str.capitalize()` uppercases the first character and lowercases the rest:

```python
'list'.capitalize()   # → 'List'
'dict'.capitalize()   # → 'Dict'
```

## Indentation as block definition

Python uses **indentation** (tabs or spaces, consistently) to delimit blocks —
there are no braces. The body of a function, an `if`, an `elif`, or an `else`
must be indented one level deeper than its header line.

## Function signature with type hints

```python
def all_thing_is_obj(object: any) -> int:
```

- `object: any` — parameter annotated as accepting any type
- `-> int` — return type annotation
- Annotations are not enforced at runtime; they serve as documentation



[return](../../README.md)
