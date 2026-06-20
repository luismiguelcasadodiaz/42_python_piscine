# ds_3_oop — Exercise 00: Findings

## Learning aims

### Abstract classes

An abstract class defines a **contract**: it declares which methods every subclass
must implement, but cannot be instantiated on its own. Trying to do so raises a
`TypeError` at runtime.

This is useful when you want to model a concept that is always specialised — a
`Character` in isolation makes no sense; only a `Stark`, a `Lannister`, etc., do.

```python
from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def die(self):
        pass
```

Any class that inherits from `Character` but does not override `die` cannot be
instantiated. The enforcement happens at runtime, not at import time.

### Inheritance

A subclass inherits all attributes and methods of its parent. It only needs to
define what is different or new. If the child's `__init__` does nothing except
forward the same arguments to the parent, it is redundant — Python will use the
parent's `__init__` automatically through the inheritance chain.

```python
class Stark(Character):
    def die(self):
        if self.is_alive:
            self.change_health()
```

`Stark` inherits `__init__`, `change_health`, and `is_alive` from `Character`
without redeclaring them.

### Instance attributes and `__dict__`

Attributes set with `self.x = value` inside `__init__` are stored per instance.
`__dict__` exposes them as a plain dictionary, which makes the object's internal
state inspectable at any time.

### Docstrings and `__doc__`

Every class and method should carry a docstring — a string literal placed
immediately after the `def` or `class` line. It is accessible at runtime via the
`__doc__` attribute, which is how peer-evaluation scripts (and humans) verify
that documentation exists.

---

## Notes on duck typing vs. abstract base classes

> *Duck typing is a programming philosophy summed up by the phrase: "If it walks
> like a duck and quacks like a duck, then it's a duck."*

In a duck-typed language like Python, what matters is not an object's declared
type, but whether it has the methods and properties you are trying to use. You
never need to declare "this object implements interface X" — you just call the
method, and if it works, it works.

This contrasts with statically-typed languages like Java or C#, where you would
need to explicitly declare that a class implements an interface before passing an instance to a function that expects one.

The tradeoff is **flexibility versus safety**. Duck typing makes code concise and adaptable — you can pass any compatible object without boilerplate — but errors only surface when the code actually runs, which can make bugs harder to catch early. That is exactly the gap that the `abc` module fills: it lets you
optionally add interface-like contracts when the flexibility becomes a liability.

### How `ABC` enforces contracts at runtime

When you decorate a method with `@abstractmethod`, Python adds its name to an
internal set called `__abstractmethods__` on the class. At instantiation time,
Python checks whether that set is empty. If it is not — meaning some abstract
methods have not been overridden — it raises a `TypeError`. This is a
**runtime** check, not a compile-time one, which is an important distinction
compared to Java or C#.

### Beyond your own classes: `register()`

The `abc` module also powers a `register()` mechanism, which lets you declare
that a class is a "virtual subclass" of an abstract base class without actually
inheriting from it. This makes `isinstance()` and `issubclass()` checks work for
classes you do not control.

---

## Notes on `super()`

### When you need `super().__init__()`

When the parent sets up attributes or logic that the child depends on. If
`Character.__init__` is where `self.first_name` and `self.is_alive` get stored,
skipping `super().__init__()` in a child means those attributes will not exist.

### When you can skip it

When the parent's `__init__` does not do anything meaningful. `Character` calls
`super().__init__()` on `ABC`, but `ABC` does not set up anything useful, so
omitting it in `Character` would still work.

If a child's `__init__` does nothing except forward the same arguments to the
parent unchanged, the whole method is redundant — Python will automatically use
the parent's `__init__` through inheritance.

[return](../../README.md)
