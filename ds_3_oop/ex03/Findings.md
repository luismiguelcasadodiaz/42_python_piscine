# ds_3_oop — Exercise 03: Findings

## Learning aims

### Operator overloading

Python lets you define how your own objects respond to standard operators
(`+`, `-`, `*`, `/`, etc.) by implementing the corresponding dunder methods.
When Python sees `v1 + 5`, it calls `v1.__add__(5)`. If the method is not
defined, Python raises a `TypeError`.

This means your objects can participate in the natural syntax of the language
without the caller needing to know anything about the internals.

### Element-wise (vectorised) operations

The operations here apply a scalar to **every element** of a list individually.
This is the foundation of vectorised thinking: instead of writing a loop at the
call site, the operation knows how to distribute itself across a sequence.

```python
v1 = calculator([0.0, 1.0, 2.0, 3.0])
v1 + 5   # → [5.0, 6.0, 7.0, 8.0]
```

This is what numerical libraries do automatically — this exercise builds the
mental model manually.

### Side-effect dunder methods (`-> None`)

Most operator overloads return a new object. Here the methods return `None` and
print the result directly. This is an intentional design constraint that
highlights the difference between:

- **Transforming** — compute and return a new value (pure, composable)
- **Acting** — compute and print, modify in place (side-effecting)

Both are valid patterns; knowing which one you are writing matters.

### Selective error handling

The subject requires handling **only** division by zero — nothing else. This
teaches restraint: guard exactly the boundaries that can fail, and trust
everything else.

```python
def __truediv__(self, object) -> None:
    if object == 0:
        raise ZeroDivisionError("Division by zero")
    for i, val in enumerate(self.data):
        self.data[i] = val / float(object)
    print(self.data)
```

### Mutable default argument pitfall

`def __init__(self, data: list = None)` — using `None` as the default and
creating the list inside the body guards against a classic Python trap: if you
write `def __init__(self, data=[])`, that single list object is shared across
**all** instances that don't pass an argument, because **default values are
evaluated ONCE at function definition time**, not at each call.

---

## Notes on dunder methods

Dunder methods (double underscore) let you define how objects behave with
built-in Python operations. There are 100+ in the data model; the most commonly
used groups:

| Group | Methods | Triggered by |
|-------|---------|--------------|
| Lifecycle | `__init__`, `__new__`, `__del__` | instantiation, GC |
| String repr | `__str__`, `__repr__` | `print()`, `repr()`, console |
| Comparison | `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__` | `==`, `!=`, `<`, `<=`, `>`, `>=` |
| Arithmetic | `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__` | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| Reflected arithmetic | `__radd__`, `__rsub__`, … | when object is on the **right** side |
| Container | `__len__`, `__getitem__`, `__setitem__`, `__contains__`, `__iter__`, `__next__` | `len()`, `[]`, `in`, `for` |
| Attribute access | `__getattr__`, `__setattr__`, `__delattr__` | `.name` access and assignment |
| Context manager | `__enter__`, `__exit__` | `with` statement |
| Callable | `__call__` | `obj()` |
| Hashing | `__hash__` | `dict` keys, `set` membership |

**Reflected versions** — when Python evaluates `5 + v1` and `int` does not know
how to add a `calculator`, it tries `v1.__radd__(5)` instead. Implementing
`__radd__` makes your objects commutative with built-in types.

A compact example tying several together:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return int((self.x**2 + self.y**2) ** 0.5)

v = Vector(3, 4)
v + Vector(1, 2)  # Vector(4, 6)
len(v)            # 5
```

[return](../../README.md)
