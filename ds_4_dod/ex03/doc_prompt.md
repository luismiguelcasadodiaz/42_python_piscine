
Four concepts to learn in this exercise:

+  1. @dataclass — boilerplate elimination
  The decorator auto-generates __init__, __repr__, and __eq__ from the field declarations. The subject explicitly
  forbids writing __str__ or __repr__ yourself — forcing you to rely on what @dataclass provides. You learn what you
  get for free and why it is useful.

+  2. field(init=False) — non-initializable computed fields
  login and id must not be settable at construction time — passing them should raise a TypeError. This requires
  marking them with field(init=False), which excludes them from the generated __init__ signature. Understanding why
  and how this works is a core part of the exercise.

+  3. __post_init__ — derived fields computed after construction
  The auto-generated __init__ sets name and surname. Then __post_init__ runs automatically and computes login (derived from name and surname) and id (a random string). You learn that @dataclass does not prevent
  post-construction logic — it just moves it to a dedicated hook.

+  4. When @dataclass is the right tool
  The contrast with a hand-written class is implicit: @dataclass is appropriate when a class is primarily a data
  container with little custom behaviour. The moment you need computed fields, controlled access, or complex
  construction logic, you add __post_init__ — and the subject shows exactly that threshold.


# `dataclass` and `field`
dataclass and field come from Python's dataclasses module, and they're used to cut down on boilerplate when writing classes that mainly exist to hold data.

## The problem they solve
Without dataclasses, a simple data-holding class looks like this:
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

That's a lot of repetitive code just to store two values.
## `@dataclass`

The decorator auto-generates `__init__`, `__repr__`, and `__eq__` for you, 
based on type-annotated class attributes:

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(3, 4)
print(p)        # Point(x=3, y=4)
print(p == Point(3, 4))   # True
```

## `@dataclass(repr=False)`
Two ways, depending on the scope you want:
1. Disable __repr__ for the whole class
Pass repr=False to the decorator itself:
```python
from dataclasses import dataclass

@dataclass(repr=False)
class Point:
    x: int
    y: int

p = Point(3, 4)
print(p)   # <__main__.Point object at 0x7f8a1c0b3d90>
```

Now Python falls back to the default object.__repr__.
2. Write your own __repr__
If you just define __repr__ yourself in the class body, dataclass will not overwrite it — dataclass only adds a method if one doesn't already exist on the class:
```python
@dataclass
class Point:
    x: int
    y: int

    def __repr__(self):
        return f"<Point at ({self.x}, {self.y})>"

p = Point(3, 4)
print(p)   # <Point at (3, 4)>
```
This is the more common pattern — you usually don't want the default object repr (which is just a memory address and not very useful), you want a custom one.


# `field()`
`field()` lets you customize how an individual attribute behaves — things a plain annotation can't express. The most common case: **mutable default values**.

```python
@dataclass
class Point:
    x: int = 0
    y: int = 0
```

This works fine for immutable defaults like `0`. But try this:

```python
@dataclass
class Group:
    members: list = []   # ❌ raises ValueError
```

Python won't let you do that, because a single list object would be shared across every instance (the classic "mutable default argument" bug). `field()` fixes it with `default_factory`:

```python
from dataclasses import dataclass, field

@dataclass
class Group:
    members: list = field(default_factory=list)
```
Now each instance gets its own fresh list.

## Other things `field()` controls
```python
@dataclass
class User:
    name: str
    id: int
    tags: list = field(default_factory=list)
    password: str = field(default="", repr=False)   # hide from __repr__
    internal_id: int = field(default=0, compare=False)  # ignore in __eq__
```

+ default — a plain (immutable) default value
+ default_factory — a zero-arg callable to produce a fresh default (lists, dicts, sets, other dataclasses)
+ repr=False — exclude the field from the auto-generated __repr__ (useful for secrets)
+ compare=False — exclude the field from __eq__/ordering
+ init=False — don't include it as an __init__ parameter

Field-level, exclude just one field from the generated __init__:
```python
@dataclass
class User:
    name: str
    id: int = field(init=False, default=0)
```
The field still exists on the instance, just isn't a constructor parameter (you'd typically set it in __post_init__ instead).

Once you use a default, the following attributes must have one default. The same that in a regular function signature.

## Quick mental model

|You want to...|Use|
|--------------|---|
|Just store a couple of plain values|type annotation only|
|Give a default like `0`, `""`, `None`|`= value`|
|Give a default that's a list/dict/set/object|`field(default_factory=...)`|
|Tweak repr/eq/init behavior per-field|`field(...)` with the relevant kwarg|


A good rule of thumb: reach for `field()` whenever a plain `=` default would either error out (mutable types) or you need finer control over a specific attribute's behavior.

## what init=False does

Let's trace exactly what init=False does.
## The key fact: init=False + plain default= skips instance assignment entirely
When a field has `init=False` and a literal `default=value` (not `default_factory`), dataclass does not generate any **assignment line** for it inside `__init__`. Instead, it leaves the default sitting as a **class attribute** (`Student.active = True`) and relies on normal Python attribute lookup: if an **instance** doesn't have `active` in its own `__dict__`, lookup falls through to the class and finds it there.

So right after construction, `active` is **not actually in** `student.__dict__` **at all** — it's only visible by fallback to the class. It only becomes a **real per-instance** entry once something explicitly does `self.active = ...` somewhere.

Compare that to `login/id` in your `__post_init__`, which are explicitly assigned (`self.login = ...`, `self.id = ...`) — those create real __dict__ entries the moment that code runs.

## Walking through output
```python
active: bool = field(init=False, default=True)   # no assignment generated in __init__
login: str = field(init=False, default="")       # same — but YOU assign it in __post_init__
id: str = field(init=False, default="")           # same — also assigned in __post_init__
```
Construction sequence for Student(name="Edward", surname="agle"):

1.- `self.name = "Edward"` → `__dict__` = `{name}`
2.- `self.surname = "agle"` → `__dict__` = `{name, surname}`
3.- `active` — **skipped**, no line generated, nothing added to `__dict__`
4.- `login`, `id` — **skipped** too, for the same reason (also `init=False` with plain default)
5.- `__post_init__()` runs:

    + `self.login = "Eagle"` → `__dict__` = `{name, surname, login}`
    + `self.id = "..."` → `__dict__` = `{name, surname, login, id}`



At this point `active'  still isn't in `__dict__` — `print(student)` reads `self.active`, which falls back to the **class attribute** True, giving you `active=True` in the repr even though it's absent from the instance dict.

Then:
```python
student.active = False
```
This is the first real write to `active` on this instance — so it's inserted **last**:
```python
{'name': ..., 'surname': ..., 'login': ..., 'id': ..., 'active': False}
```

Exactly matching what you observed, every single time, regardless of the @property experiments.

## Key takeaway
`__dict__` order = order of **first actual assignment**, not field-declaration order. `init=False` with a plain `default=` actively delays (or entirely skips) that first assignment, decoupling instance-dict order from class-body order.

## How to make it eager again
If you want an `init=False` field to actually get a **real instance entry immediately**, at its declared position, use `default_factory` instead of `default` — even for a constant:
```python
active: bool = field(init=False, default_factory=lambda: True)
```
For `default_factory`, dataclass always generates an assignment line in `__init__`, regardless of `init=True/False` — so this field would show up in `__dict__` right after `surname`, in its declared position, just like a normal field would.


###     active: bool = field(init=False, default=True)

Defines a class attribute

```bash
-------------Before post init......................
Student(name='Edward', surname='agle', active=True, login='', id='')
{'name': 'Edward', 'surname': 'agle'}
-------------after post init......................
Student(name='Edward', surname='agle', active=True, login='Eagle', id='jqicgmesoeiyxag')
{'name': 'Edward', 'surname': 'agle', 'login': 'Eagle', 'id': 'jqicgmesoeiyxag'}
-------------Before change active......................
Student(name='Edward', surname='agle', active=True, login='Eagle', id='jqicgmesoeiyxag')
{'name': 'Edward', 'surname': 'agle', 'login': 'Eagle', 'id': 'jqicgmesoeiyxag'}
-------------after change active......................
Student(name='Edward', surname='agle', active=False, login='Eagle', id='jqicgmesoeiyxag')
{'name': 'Edward', 'surname': 'agle', 'login': 'Eagle', 'id': 'jqicgmesoeiyxag', 'active': False}
```
### active: bool = field(default=True)

defines an instance attribute

```bash
-------------Before post init......................
Student(name='Edward', surname='agle', active=True, login='', id='')
{'name': 'Edward', 'surname': 'agle', 'active': True}
-------------after post init......................
Student(name='Edward', surname='agle', active=True, login='Eagle', id='oslvgoayeypffhx')
{'name': 'Edward', 'surname': 'agle', 'active': True, 'login': 'Eagle', 'id': 'oslvgoayeypffhx'}
-------------Before change active......................
Student(name='Edward', surname='agle', active=True, login='Eagle', id='oslvgoayeypffhx')
{'name': 'Edward', 'surname': 'agle', 'active': True, 'login': 'Eagle', 'id': 'oslvgoayeypffhx'}
-------------after change active......................
Student(name='Edward', surname='agle', active=False, login='Eagle', id='oslvgoayeypffhx')
{'name': 'Edward', 'surname': 'agle', 'active': False, 'login': 'Eagle', 'id': 'oslvgoayeypffhx'}
```