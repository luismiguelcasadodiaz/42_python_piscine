# ds_4_dod — Exercise 03: Findings

## Learning aims

### `@dataclass` — boilerplate elimination

Without dataclasses, a simple data-holding class requires repetitive boilerplate:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
```

`@dataclass` auto-generates `__init__`, `__repr__`, and `__eq__` from
type-annotated class attributes:

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(3, 4)
print(p)               # Point(x=3, y=4)
print(p == Point(3, 4))  # True
```

The subject explicitly forbids writing `__str__` or `__repr__` — forcing you
to rely on what `@dataclass` provides and understand what you get for free.

### `field(init=False)` — non-initializable fields

`field(init=False)` excludes an attribute from the generated `__init__`
signature. Attempting to pass it raises a `TypeError`:

```python
Student(name="Edward", surname="agle", id="toto")
# TypeError: Student.__init__() got an unexpected keyword argument 'id'
```

This is how `login` and `id` are protected from external construction — they
are computed internally, not supplied by the caller.

### `__post_init__` — derived fields computed after construction

`__post_init__` runs automatically after the generated `__init__` completes.
It is the designated hook for computing derived fields:

```python
def __post_init__(self):
    self.login = self.name[0].upper() + self.surname
    self.id = generate_id()
```

`@dataclass` does not prevent post-construction logic — it just moves it to a
dedicated, named hook rather than cluttering `__init__`.

### When `@dataclass` is the right tool

`@dataclass` is appropriate when a class is primarily a **data container**. The
moment you need computed fields or controlled access, you add `__post_init__`
— this exercise sits exactly at that threshold.

---

## Deep dive: `field(init=False, default=)` vs `field(default=)`

The debugging output revealed a non-obvious distinction between these two forms.

### `field(init=False, default=True)` — class attribute, lazy instance entry

When a field has `init=False` **and** a plain `default=value` (not
`default_factory`), dataclass does **not** generate any assignment line for it
inside `__init__`. Instead, the default sits as a **class attribute**
(`Student.active = True`). Python's normal attribute lookup falls through to
the class if the instance `__dict__` does not have it.

**Construction sequence for `Student(name="Edward", surname="agle")`:**

| Step | What happens | `__dict__` |
|------|-------------|------------|
| 1 | `self.name = "Edward"` | `{name}` |
| 2 | `self.surname = "agle"` | `{name, surname}` |
| 3 | `active` — **skipped**, no line generated | `{name, surname}` |
| 4 | `login`, `id` — **skipped** too | `{name, surname}` |
| 5 | `__post_init__`: `self.login = "Eagle"` | `{name, surname, login}` |
| 6 | `__post_init__`: `self.id = "..."` | `{name, surname, login, id}` |

After construction, `active` is **not in `__dict__`** — `print(student)` reads
`self.active`, falls back to the class attribute `True`, and shows `active=True`
in the repr even though it is absent from the instance dict.

Then `student.active = False` is the **first real write** to `active` on this
instance — so it is inserted **last**:

```
{'name': ..., 'surname': ..., 'login': ..., 'id': ..., 'active': False}
```

### `field(default=True)` (with `init=True`) — instance attribute, eager entry

When `init=True` (the default), dataclass **does** generate an assignment line.
`active` becomes a real instance attribute immediately and appears in `__dict__`
at its declared position:

```
Before __post_init__:
{'name': 'Edward', 'surname': 'agle', 'active': True}

After __post_init__:
{'name': 'Edward', 'surname': 'agle', 'active': True, 'login': 'Eagle', 'id': '...'}

After student.active = False:
{'name': 'Edward', 'surname': 'agle', 'active': False, 'login': 'Eagle', 'id': '...'}
```

### Key takeaway

> **`__dict__` order = order of first actual assignment, not field-declaration order.**

`init=False` with a plain `default=` actively delays (or entirely skips) that
first assignment, decoupling instance-dict order from class-body order.

**To force eager instance assignment for an `init=False` field**, use
`default_factory` instead — even for a constant:

```python
active: bool = field(init=False, default_factory=lambda: True)
```

`default_factory` always generates an assignment line in `__init__`, so `active`
would appear in `__dict__` right after `surname`, at its declared position.

---

## Notes on `field()` options

| Option | Use |
|--------|-----|
| `default=value` | plain immutable default |
| `default_factory=callable` | fresh mutable default per instance (list, dict, lambda) |
| `init=False` | exclude from `__init__` — set in `__post_init__` instead |
| `repr=False` | exclude from auto-generated `__repr__` (e.g. passwords) |
| `compare=False` | exclude from `__eq__` / ordering |

**Mutable default pitfall** — `members: list = []` raises `ValueError` in a
dataclass. Use `field(default_factory=list)` instead. Each instance then gets
its own fresh list.

**Default ordering rule** — once a field has a default, all following fields
must also have one. Same rule as regular function signatures.

## Notes on `@dataclass` options

`@dataclass(repr=False)` disables the auto-generated `__repr__`, falling back
to `object.__repr__` (a memory address). More commonly, just define `__repr__`
yourself — dataclass will not overwrite a method that already exists on the
class:

```python
@dataclass
class Point:
    x: int
    y: int

    def __repr__(self):
        return f"<Point at ({self.x}, {self.y})>"
```

[return](../../README.md)
