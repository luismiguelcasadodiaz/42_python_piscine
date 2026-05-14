# Generators, yield, and Terminal Control — Findings

## `yield` — generator functions

Adding `yield` to a function makes it a **generator function**.
Calling it does NOT execute the body — it returns a generator object.
The body runs step by step only when iterated:

```python
def ft_tqdm(lst: range) -> None:
    for current, e in enumerate(lst):
        yield e          # pauses here, hands e to the for loop, resumes on next iteration
        # code after yield runs before the next yield
```

| Regular function | Generator function |
|------------------|--------------------|
| Runs fully on call | Body runs on each iteration |
| Returns once | `yield`s many times |
| Stores result in memory | Produces values on demand (lazy) |

This is what makes `ft_tqdm` work as a drop-in replacement for `tqdm` in a
`for` loop — the caller iterates it exactly like any other iterator.

## `enumerate()`

Produces `(index, value)` pairs — cleaner than maintaining a manual counter:

```python
for current, e in enumerate(lst):
    ...
```

Equivalent to:
```python
current = 0
for e in lst:
    ...
    current += 1
```

## `\r` — in-place terminal update

`\r` (carriage return) moves the cursor to the start of the **current line**
without advancing to a new line. Combined with `end=""` and `flush=True`,
it overwrites the same line on every update:

```python
print("\r" + chunk1 + chunk3, end="", flush=True)
```

This creates the live progress bar effect — no scrolling, just in-place rewrite.

## `print(flush=True)` — forced stdout flush

Python buffers stdout by default — output is held in memory and written in
batches. `flush=True` forces immediate delivery to the terminal:

```python
print("\r...", end="", flush=True)
```

Without it, the progress bar would not update live — it might only appear at
the end of the loop when the buffer is finally flushed.

## `os.get_terminal_size()` — adaptive layout

Reading the terminal width at runtime allows the bar to scale to any screen:

```python
columns = os.get_terminal_size().columns
barchar = columns - fixchar - (varchar * 2)
```

The fixed characters (percentage, counters, brackets, timing) are subtracted,
and the remainder is given to the progress bar itself.

## Time estimation math

Three values are computed from elapsed time and progress:

```python
elapsed_seconds = time.time() - t0
lasting_seconds = all * elapsed_seconds / (current + 1)   # estimated total
remain_seconds  = lasting_seconds - elapsed_seconds        # estimated left
ite_second      = (current + 1) / elapsed_seconds         # throughput
```

This is proportional estimation: if `k` items took `t` seconds, then `n` items
will take `n * t / k` seconds total.

## `time.strftime()` / `time.gmtime()` — duration formatting

Elapsed and remaining seconds are formatted as `MM:SS`:

```python
time.strftime("%M:%S", time.gmtime(elapsed_seconds))
```

`time.gmtime()` converts seconds to a `struct_time` in UTC.
`time.strftime()` formats it. Using UTC avoids timezone offsets distorting
the duration display.

## Dynamic f-string width specifiers

The counter width adapts to the total number of items (1 digit for 9, 3 for 333):

```python
varchar = len(str(all))                    # e.g. 3 for 333
f"{current + 1:{varchar}d}"               # right-aligned, width = varchar
```

A variable can be used as the format width by placing it inside `{}` within
the format spec — a powerful f-string feature.

## Benchmarking against a production library

The tester runs both `ft_tqdm` and the real `tqdm` back to back:

```python
for elem in ft_tqdm(range(3333)):
    sleep(0.005)
for elem in tqdm(range(3333)):
    sleep(0.005)
```

This is the 42 "recode before you use" pattern taken further — not just
reimplementing, but **measuring your implementation against the original**
to understand the gap and the cost of real-world optimisation.



[return](../../README.md)
