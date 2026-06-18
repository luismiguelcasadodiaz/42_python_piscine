# ds_4_dod — Exercise 01: Findings

## Learning aims

### Closures

A closure is a function that **remembers values from its enclosing scope** even
after that scope has finished executing. It happens when an inner function
references a variable from an outer function:

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor   # factor is captured from outer scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

double(5)   # 10 — factor=2 is still alive inside double
triple(5)   # 15 — factor=3 is still alive inside triple
```

After `make_multiplier` returns, its local variable `factor` would normally be
gone. Because `multiply` references it, Python keeps it alive — that is the
closure. The inner function "closes over" the variable.

### Returning a function vs. calling a function

`outer` returns `inner` as an **object** — no parentheses:

```python
return inner      # returns the function itself
return inner()    # would call it immediately and return its result
```

The caller stores the function object and decides when to invoke it:

```python
my_counter = outer(3, square)   # stores the closure
my_counter()                    # invokes it — square(3) = 9
my_counter()                    # invokes again — square(9) = 81
```

This is the foundation of higher-order functions: functions that produce other
functions as their return value.

### Mutable closure state with `nonlocal`

By default, an inner function can only **read** a variable from the enclosing
scope. To **reassign** it, the `nonlocal` keyword is required:

```python
def counter():
    count = 0
    def increment():
        nonlocal count   # without this, count += 1 would raise UnboundLocalError
        count += 1
        return count
    return increment

c = counter()
c()   # 1
c()   # 2
```

In this exercise, `count` starts as `x` and is updated on every call to
`inner`. Without `nonlocal`, the assignment `count = function(count)` would
create a new local variable inside `inner` instead of updating the one in
`outer`'s scope.

### Independent instances, no shared state

Each call to `outer` creates a **separate closure** with its own `count`:

```python
my_counter      = outer(3, square)   # count=3, independent
another_counter = outer(1.5, pow)    # count=1.5, independent
```

Calling `my_counter()` does not affect `another_counter` and vice versa. This
is the key advantage of closures over global variables: state is scoped
privately to each instance.

### State without global variables

The subject forbids `global`. The closure is the clean alternative: state lives
in the enclosing function's local scope, which persists as long as the inner
function is alive — without polluting the module's global namespace.

---

## Notes on closures

You can inspect what a closure captured using `__closure__` — each captured
variable is stored in a cell object:

```python
def outer(x):
    def inner():
        return x
    return inner

f = outer(42)
f.__closure__[0].cell_contents   # 42
```

Closures are useful for:
- **Factories** — producing configured functions (like `make_multiplier`)
- **Decorators** — wrapping functions with extra behaviour
- **Callbacks** — passing behaviour into event systems
- **Stateful iterators** — maintaining position without a class

The pattern in this exercise — outer function sets up state, inner function
mutates and returns it — is the functional equivalent of a class with a single
method and a single instance variable.

[return](../../README.md)
