# ds_3_oop — Exercise 01: Findings

## Learning aims

### Sibling subclasses extending a shared abstract parent

Two classes (`Baratheon`, `Lannister`) can independently inherit from the same
abstract parent (`Character`), each satisfying the abstract contract (`die`) and
adding their own attributes on top.

The parent's `__init__` is extended — not replaced — by calling `super().__init__()` 
first and then setting the subclass-specific attributes:

```python
class Baratheon(Character):
    def __init__(self, first_name: str):
        super().__init__(first_name)      # honours the parent setup
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
```

### `@classmethod` as an alternative constructor (factory method)

A class method receives the class itself (`cls`) as its first argument instead of
an instance. This lets you define named construction paths that sit at the class
level, not the instance level:

```python
@classmethod
def create_lannister(cls, first_name: str, is_alive: bool):
    return cls(first_name, is_alive)
```

Calling `Lannister.create_lannister("Jaine", True)` is equivalent to
`Lannister("Jaine", True)` here, but the pattern becomes valuable when the
factory needs to validate, transform, or fetch data before creating the object —
and when you want the creation path to have a meaningful name.

---

## Notes on `__str__()` and `__repr__()`

Both control how an object is represented as a string, but they serve different
audiences.

| Method | Audience | Called by |
|--------|----------|-----------|
| `__str__` | End user — readable | `print()`, `str()`, f-strings `f"{obj}"` |
| `__repr__` | Developer — unambiguous | `repr()`, console inspection |

If `__str__` is not defined, Python **falls back** to `__repr__`. The reverse is
not true. This means if you only define one, `__repr__` is the more useful choice
— it covers both cases.

```python
ned = Character("Ned", False)
print(ned)        # calls __str__ → "Ned is dead"
print(repr(ned))  # calls __repr__ → "Character('Ned', False)"
```

### The `eval(repr(obj))` convention

The convention is that `__repr__` should return a string that, when passed to
`eval()`, recreates the object:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(3, 5)
p2 = eval(repr(p))   # creates a new Point(3, 5)
```

This is a convention, not a requirement — for complex objects it is not always
possible. But when it is achievable, it is the right default. The exercise
demonstrates this: `Lannister.__repr__` returns `Lannister('Jaine', True)`, which
`eval()` can execute to reconstruct the object.

---

## Notes on decorators

A decorator is a function that takes another function as input, adds behavior to
it, and returns a modified version — without changing the original function's
code. The `@` syntax is shorthand:

```python
@my_decorator
def say_hello():
    print("Hello!")

# equivalent to:
say_hello = my_decorator(say_hello)
```

Common uses: logging, timing, access control, caching (`lru_cache`), retrying.

`@classmethod` and `@abstractmethod` are both built-in decorators — they change
the nature of the method they wrap. `@classmethod` replaces the implicit `self`
with `cls`; `@abstractmethod` marks the method as a contract that subclasses must
fulfill.

---

## Notes on the factory method pattern

A factory method constructs and returns an object instead of having the caller
use the constructor directly. It gives the creation path a meaningful name and
lets you offer multiple construction paths without multiple `__init__` signatures:

```python
c1 = Color(255, 0, 0)           # direct
c2 = Color.from_hex("#FF0000")   # factory — named, accepts a different input form
c3 = Color.from_name("red")      # factory — named, looks up a value
```

This pattern appears throughout the standard library: `dict.fromkeys()`,
`datetime.fromtimestamp()`, `int.from_bytes()`.

---

## Notes on stale docstrings

A stale docstring no longer accurately describes the code it documents. It occurs
when behavior is updated — parameters added or removed, return values changed —
but the docstring is not updated alongside.

Stale docstrings are considered **worse than no docstring at all** because they
create false confidence. A developer trusting a stale docstring may pass wrong
arguments or mishandle return values.

In this exercise, `Baratheon.__str__` was updated to delegate to `__repr__` but
its docstring still read *"Returns: None — this method is not implemented"* — a
textbook stale docstring.

[return](../../README.md)
