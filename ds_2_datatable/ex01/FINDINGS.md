# Drawing a Country — Findings

## `set_index()` — turning a column into the row label

`set_index()` promotes an existing column to become the DataFrame's row index,
enabling fast label-based lookup with `.loc`:

```python
df = pd.DataFrame({
    "country":    ["Spain", "France", "Italy"],
    "population": [47, 67, 59]
})
df = df.set_index("country")
```

Before:
```
   country  population
0    Spain          47
1   France          67
2    Italy          59
```

After:
```
         population
country
Spain            47
France           67
Italy            59
```

The "country" column is no longer a regular column — it is the row label.
`df.loc["Spain"]` now selects Spain's row directly by name.

Key behaviours:
- Returns a **new** DataFrame by default; use `inplace=True` or reassign
- `df.reset_index()` moves the index back into a regular column
- Multiple columns can form a `MultiIndex`: `df.set_index(["country", "year"])`

---

## Row selection: `.loc` vs boolean mask

Two equivalent approaches to isolate one country:

```python
# Label-based (after set_index)
row = df.loc["France"]

# Boolean mask (works on the original column)
row = df[df["country"] == "France"]
```

Both return the same data; `.loc` is more concise when the index is already
set, while boolean masks are more flexible for complex conditions.

---

## `.loc[label]` on a single row returns a Series

When a DataFrame has `n` columns and you select one row with `.loc[label]`,
pandas returns a **Series** — not a single-row DataFrame:

```python
# data: 192 rows × 301 columns (countries × years)
data_plot = data.loc["France"]
# data_plot: Series of 301 entries — years become the index
```

The former column names become the Series index, and the cell values become
the data. This is the implicit transpose: a row becomes a column-like object
ready for plotting.

---

## Wide-format data and column dtype

The Gapminder CSV stores years as column names. After `set_index("country")`,
the remaining columns are year labels. Their dtype depends on the CSV content
— they are often **strings** (`"1800"`, `"1801"`, …), not integers.

`.loc` preserves the original dtype without conversion. If the index type is
string, the x-axis tick labels on a plot will be strings and matplotlib may
show every single one — producing an unreadable axis.

Convert to integers explicitly:

```python
data_plot.index = data_plot.index.astype(int)
```

With an integer index, `plt.plot()` treats the x-axis as a numeric scale and
automatically shows only a manageable subset of labels.

---

## Controlling x-axis tick density

With ~300 data points, the default tick behaviour can still crowd the axis.
`MaxNLocator` limits the number of ticks shown:

```python
ax = plt.gca()                          # get current axes
ax.xaxis.set_major_locator(plt.MaxNLocator(nbins=6))
```

`nbins=6` asks matplotlib to place at most 6 tick marks, spaced at "nice"
intervals.

---

## Minimum anatomy of a labelled line chart

The subject requires a title and a label for each axis:

```python
plt.plot(data_plot)
plt.title(f"{country} Life Expectancy Projections")
plt.ylabel("Life Expectancy")
plt.xlabel("Year")
plt.show()
```



[return](../../README.md)
