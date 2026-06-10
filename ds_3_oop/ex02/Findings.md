# ds_3_oop — Exercise 02: Findings

## Learning aims

### Multiple inheritance and the diamond problem

When a class inherits from two parents that themselves share a common ancestor,
the inheritance graph forms a diamond:

```
      Character
      /        \
 Baratheon   Lannister
      \        /
        King
```

The problem: when `King` calls a method defined in both `Baratheon` and
`Lannister`, which version wins? And how is `Character.__init__` called — once
or twice?

### Method Resolution Order (MRO) and C3 linearization

Python resolves this through the **Method Resolution Order** — a flat, linear
sequence of classes that defines the exact lookup order for any attribute or
method call. It is computed at class definition time using the **C3
linearization** algorithm.

For `King(Baratheon, Lannister)` the MRO is:

```
King → Baratheon → Lannister → Character → ABC → object
```

C3 guarantees three properties:
- Children are checked before parents.
- The order you list parents in the class declaration is preserved (left to right).
- No class appears before all of its subclasses.

If these constraints cannot all be satisfied simultaneously, Python raises a
`TypeError` **at class definition time** — before any object is created.

You can inspect the MRO directly:

```python
print(King.__mro__)
# (<class 'King'>, <class 'Baratheon'>, <class 'Lannister'>,
#  <class 'Character'>, <class 'ABC'>, <class 'object'>)
```

**Declaration order matters.** Swap `Baratheon` and `Lannister` and the winner
changes:

```python
class King(Baratheon, Lannister):  # Baratheon wins
class King(Lannister, Baratheon):  # Lannister wins
```

### Controlling which sibling's method runs

| Goal | Technique |
|------|-----------|
| Default winner | List that sibling first in the class declaration |
| Force a specific sibling | Call `SiblingClass.method(self)` directly |
| Skip a sibling in the MRO | `super(ClassToSkip, self).method()` |
| Run all siblings | Have every class call `super()` (cooperative pattern) |

**Direct class reference** — most explicit:
```python
class King(Baratheon, Lannister):
    def greet(self):
        return Lannister.greet(self)  # bypasses MRO, forces Lannister
```

**`super()` with arguments** — skip to a point in the MRO:
```python
class King(Baratheon, Lannister):
    def greet(self):
        return super(Baratheon, self).greet()  # skips Baratheon → lands on Lannister
```

**Cooperative inheritance** — have every class call `super()` so the chain
propagates through the entire MRO:
```python
class C1(Base):
    def greet(self):
        return "C1, " + super().greet()

class C2(Base):
    def greet(self):
        return "C2"

class Diamond(C1, C2):
    pass

Diamond().greet()  # "C1, C2"
```

### `@property` and the private backing store

Properties let you control read/write access to an attribute without changing
how callers interact with it. The public interface stays `obj.eyes = "blue"`;
the property intercepts that assignment and applies whatever logic you need.

```python
@property
def eyes(self) -> str:
    return self._eyes

@eyes.setter
def eyes(self, color: str) -> None:
    self._eyes = color
```

**Why the underscore?** The property name (`eyes`) and the stored attribute must
differ. If you write `self.eyes = color` inside the setter, Python calls the
setter again — infinite recursion. `self._eyes` is a plain, separate attribute
where the data actually lives. The property is the public door; `_eyes` is the
back room.

The single underscore `_eyes` is a Python convention meaning "internal — do not
touch directly." Nothing enforces it; it is a signal to other developers.
Callers always use `king.eyes = "green"`, which goes through the setter. They
never need to know `_eyes` exists.

**Side effect on `__dict__`:** because the data is stored in `_eyes` and
`_hairs`, `__dict__` shows those private names rather than `eyes` and `hairs`.
This is an inherent trade-off of the property/backing-store pattern.

### Explicit getters/setters vs. `@property`

Java-style `get_eyes()` / `set_eyes()` methods are unpythonic. The Pythonic
default is to expose attributes directly and only add a `@property` if you later
need validation or transformation — without changing the caller's code at all.

This exercise is a special case: the subject's tester requires `get_eyes()` and
`set_eyes()` by name, so both exist alongside the property. In real code you
would use one or the other, not both.

---

## Notes on MRO in practice

The MRO is not just a tie-breaking rule — it is the complete lookup chain for
**every** attribute and method call, including `__init__`. When `King.__init__`
calls `super().__init__(first_name, is_alive)`, `super()` follows the MRO:
`Baratheon.__init__` runs next. If `Baratheon.__init__` also called
`super().__init__()`, it would forward to `Lannister.__init__`, and so on up to
`Character`. This cooperative chaining ensures `Character.__init__` is called
exactly once, regardless of how many paths lead to it.

[return](../../README.md)
