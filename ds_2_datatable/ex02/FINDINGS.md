# Comparing Countries — Findings

## Column range slicing — filtering years

The Gapminder CSV contains year columns from 1800 to beyond 2100. The subject
requires only 1800–2050. To select a contiguous column range use `get_loc()`
to convert label to position, then slice by position:

```python
start = data.columns.get_loc("1800")
end   = data.columns.get_loc("2050")
cols  = ["country"] + list(data.columns[start:end + 1])
data_plot = data[cols]
```

`get_loc()` returns the integer position of a column name — like finding the
index of an item in a list. It translates a label into a position, enabling
`iloc`-style slicing on column names.

An alternative when the "country" column is already the index:

```python
data_plot = data.loc[:, "1800":"2050"]
```

---

## `iloc` vs `loc`

| | `loc` | `iloc` |
|---|---|---|
| Selects by | **label** | **integer position** |
| Syntax | `df.loc["Spain"]` | `df.iloc[0]` |
| Slice end | **inclusive** | exclusive |

The distinction matters when the index is not `0, 1, 2…` — for example when
years (`1800`, `1801`, …) are the index. `iloc[0]` always means "first entry"
regardless of the label; `loc[1800]` means "the entry labelled 1800".

Works on DataFrames with two dimensions: `df.iloc[row, col]`.

---

## `.loc[label]` returns a Series; `.loc[[label]]` returns a DataFrame

`loc` with a **single label** flattens the result to a Series — the column
names become the index:

```python
data.loc["Spain"]
# 1800    29.5
# 1801    29.5
# dtype: object
```

`loc` with a **list** keeps the table structure:

```python
data.loc[["Spain"]]           # single-row DataFrame
data.loc[["Spain", "Italy"]]  # two-row DataFrame
```

The double brackets `[[ ]]` say "give me a subset of rows" (DataFrame); single
brackets `[ ]` say "give me this exact row" (Series).

---

## Two series vs DataFrame for multi-line plots

**Two Series** — explicit control over each line:

```python
spain  = data.loc["Spain"]
france = data.loc["France"]
plt.plot(spain.index,  spain.values,  label="Spain")
plt.plot(france.index, france.values, label="France")
plt.legend()
plt.show()
```

Each `plt.plot()` call **adds** to the current figure — calls are cumulative
until `plt.show()` or `plt.clf()`. This implicit state is a common source of
confusion for beginners.

**DataFrame with `.plot()`** — quick exploration:

```python
data_plot = data.loc[["Spain", "France"]].T  # transpose: years→rows
data_plot.plot()
plt.show()
```

`.T` transposes so countries become columns and years become rows — the shape
matplotlib expects for a multi-line plot. Less control over individual lines.

---

## `plt.legend()` — labels must be set first

`plt.legend()` reads the `label=` argument from each `plt.plot()` call.
Without labels, the legend has nothing to show:

```python
plt.plot(x, y, label="France")   # label must be set here
plt.legend()                      # then legend picks it up
```

If labels were forgotten, they can be passed directly:
`plt.legend(["Spain", "France"])` — but this is fragile (order-dependent).

Common options:

```python
plt.legend(loc="upper left")    # position: upper/lower/center + right/left/best
plt.legend(fontsize=12)         # text size
plt.legend(frameon=False)       # remove the box border
```

---

## Y-axis formatting — `FuncFormatter`

Raw population values (`60000000`) are unreadable as tick labels. Two
approaches:

```python
# Option 1 — scale the data before plotting
series / 1_000_000           # plot in millions, label axis "Population (M)"

# Option 2 — custom formatter (keeps raw values, formats labels)
plt.gca().yaxis.set_major_formatter(
    plt.FuncFormatter(lambda v, p: f"{v/1e6:.0f}M"))
```

`FuncFormatter` takes a function with two arguments: the tick value `v` and
its position `p` (position is rarely needed). It returns the string to display.

---

## Parsing abbreviated population values

Gapminder encodes population with suffix letters (`"10.5M"`, `"300K"`,
`"1.2B"`). Parse them with `.apply()` and a suffix-aware lambda:

```python
series.apply(
    lambda x: int(
        float(x[:-1]) * (
            1_000_000_000 if x[-1] == "B" else
            1_000_000     if x[-1] == "M" else
            1_000         if x[-1] == "K" else 1)
        if x[-1] in ("B", "M", "K") else int(x))
)
```

The guard `if x[-1] in ("B", "M", "K")` must come **before** stripping the
last character — otherwise bare integers like `"1234"` would have their last
digit stripped. Suffix matching is case-sensitive; `"K"` and `"k"` are
different characters.

---

## Numeric literals with underscores — PEP 515

Python 3.6+ allows underscores as visual separators in numeric literals.
They are ignored by the interpreter:

```python
1_000_000     # same as 1000000
1_000_000.50  # floats work too
10_000_000_000
```

Any grouping is valid, though groups of three (matching comma notation) are
conventional. Makes large numbers readable at a glance.



[return](../../README.md)
