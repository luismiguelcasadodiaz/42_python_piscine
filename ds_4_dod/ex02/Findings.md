# ds_4_dod — Exercise 02: Findings

## Learning aims

### Decorator factory — three levels of nesting

A **decorator factory** is a function that returns a decorator. It is what you
use when your decorator needs to accept a configuration argument.

**Regular decorator** — takes a function directly (two levels):

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("before")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello():
    print("hello")
```

**Decorator factory** — takes arguments, then returns a decorator (three levels):

```python
def repeat(n):               # factory: receives the config
    def decorator(func):     # actual decorator: receives the function
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("hello")

say_hello()   # prints "hello" three times
```

`@repeat(3)` works because Python first calls `repeat(3)`, which returns a
decorator, and then applies that decorator to `say_hello` — equivalent to:

```python
say_hello = repeat(3)(say_hello)
```

In this exercise the three levels are:

```
callLimit(limit)          ← factory: receives limit
  └─ callLimiter(function) ← decorator: receives the function
       └─ limit_function(*args, **kwds) ← wrapper: runs on each call
```

### The wrapper pattern

`limit_function(*args, **kwds)` sits in front of the original function. It
decides whether to call the original or block it. Using `*args`/`**kwds` makes
the wrapper **transparent to any function signature** — the caller does not know
or care that a wrapper is involved.

### Closure-based call counter

`count` starts at `0` in `callLimit`'s scope and is shared between
`callLimiter` and `limit_function` via the closure. `nonlocal` is declared
inside `limit_function` — the only place where `count` is actually modified:

```python
count = 0                          # lives in callLimit's scope

def limit_function(*args, **kwds):
    nonlocal count                 # needed here: count is reassigned
    if count != limit:
        function(*args, **kwds)
        count += 1
    else:
        print(f"Error: {function} call too many times")
```

Each `@callLimit(n)` application creates a **fresh closure** with its own
`count`. Two separately decorated functions have independent counters — `f` and
`g` do not share state.

### The `@` syntax as shorthand

`@callLimit(3)` before `def f()` is exactly equivalent to:

```python
f = callLimit(3)(f)
```

Two calls in sequence: `callLimit(3)` returns `callLimiter`; `callLimiter(f)`
returns `limit_function`, which replaces `f` in the namespace. Understanding
this equivalence unwraps any decorator factory mentally.

---

## Notes on decorator factories in the wild

Common real-world examples:

- `@app.route("/path")` in Flask — factory receives the URL path
- `@pytest.mark.parametrize(...)` — factory receives test parameters
- `@functools.lru_cache(maxsize=128)` — factory receives cache size

All follow the same three-level structure: factory → decorator → wrapper.

---

## Summary — closure concepts across ex01 and ex02

| Concept | ex01 | ex02 |
|---------|------|------|
| Inner function captures outer state | `count` accumulates results | `count` tracks call number |
| `nonlocal` to mutate captured variable | `count = function(count)` | `count += 1` |
| Returns the inner function as an object | `return inner` | `return limit_function` |
| Independent instances per call | two counters, no shared state | `f` and `g` independent |
| Forbidden global variable replaced by | closure | closure |

The decorator pattern is a closure with a specific structure and purpose: the
outer function configures, the inner function acts.

[return](../../README.md)
