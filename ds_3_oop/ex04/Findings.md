# ds_3_oop — Exercise 04: Findings

## Learning aims

### `@staticmethod` — class as a namespace

When all methods are static, the class is never instantiated — it serves purely
as a logical grouping for related utility functions:

```python
calculator.dotproduct(a, b)
calculator.add_vec(a, b)
calculator.sous_vec(a, b)
```

No `calculator()` object is created. The class is just a namespace that keeps
these functions organised and prevents them from polluting the module scope.

A static method receives **no implicit first argument** — no `self`, no `cls`.
It is a regular function that happens to live inside a class.

### Vector-vector operations vs. vector-scalar

Ex03 applied a single scalar to every element of one vector. Ex04 operates on
two vectors of equal length simultaneously:

| Operation | Formula | Result type |
|-----------|---------|-------------|
| Dot product | `sum(V1[i] * V2[i])` | scalar |
| Element-wise add | `[V1[i] + V2[i] for i]` | vector |
| Element-wise subtract | `[V1[i] - V2[i] for i]` | vector |

The dot product is the key new concept: it collapses two vectors into a single
number by summing the products of corresponding elements.

### Asserting preconditions

The subject guarantees vectors will always have identical sizes, so no error
handling is required. Using `assert` to check this anyway is a good defensive
habit — it documents the assumption and crashes loudly if it is ever violated,
rather than silently producing a wrong result from a mismatched zip.

---

## Notes on `@staticmethod` vs `@classmethod`

Both allow calling a method without instantiating the class, but they differ in
what they receive:

| Feature | `@staticmethod` | `@classmethod` |
|---------|----------------|----------------|
| Receives `self` (instance)? | No | No |
| Receives `cls` (class)? | No | Yes |
| Access instance attributes? | No | No |
| Access class attributes? | No | Yes |
| Call without instantiating? | Yes | Yes |

**`@staticmethod`** — utility or helper that needs neither the instance nor the
class. Pure function, namespaced inside the class:

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

MathUtils.add(3, 5)  # → 8
```

**`@classmethod`** — needs the class itself, typically for factory methods or
accessing class-level state:

```python
class Dog:
    species = "Canis lupus"

    @classmethod
    def get_species(cls):
        return cls.species

Dog.get_species()  # → "Canis lupus"
```

### When to use which

Use `@staticmethod` when the method is a utility that does not need class or
instance data — it could have been a module-level function, but belongs
conceptually with the class.

Use `@classmethod` when the method needs to read or modify class-level state, or
when it serves as an alternative constructor (factory method):

```python
class Date:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split("-"))
        return cls(year, month, day)

d = Date.from_string("2026-06-14")
```

### The three decorator types side by side

```python
class Example:
    class_var = "shared"

    def instance_method(self):      # receives the instance
        return self.class_var

    @classmethod
    def class_method(cls):          # receives the class
        return cls.class_var

    @staticmethod
    def static_method():            # receives nothing
        return "no access to class or instance"
```

[return](../../README.md)
