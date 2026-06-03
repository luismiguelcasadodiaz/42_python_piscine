# Loading a Dataset — Findings

## The pandas DataFrame

A `DataFrame` is the core two-dimensional data structure in pandas — a
labeled, size-mutable table of rows and columns, analogous to a spreadsheet
or SQL table.

```python
import pandas as pd

df = pd.DataFrame({
    "name":  ["Alice", "Bob", "Carol"],
    "age":   [30, 25, 35],
    "score": [88.5, 92.0, 79.3]
})
```

| | name | age | score |
|-|------|-----|-------|
| 0 | Alice | 30 | 88.5 |
| 1 | Bob | 25 | 92.0 |
| 2 | Carol | 35 | 79.3 |

Each column is a `pd.Series` — a one-dimensional labeled array. Row labels
form the **Index**, which defaults to `0, 1, 2…` but can be dates, strings,
or any hashable value.

DataFrames provide vectorised operations (no explicit loops), built-in label
alignment, and tight integration with NumPy, Matplotlib, and scikit-learn.

### Common operations at a glance

| Category | Methods |
|---|---|
| Inspecting | `df.head()`, `df.info()`, `df.describe()`, `df.shape`, `df.dtypes` |
| Selecting | `df["col"]`, `df.loc[label]`, `df.iloc[pos]`, `df[df["age"] > 25]` |
| Transforming | `df.sort_values()`, `df.groupby()`, `df.apply()`, `df.merge()`, `df.pivot_table()` |
| Cleaning | `df.dropna()`, `df.fillna()`, `df.rename()`, `df.drop_duplicates()` |
| I/O | `pd.read_csv()`, `pd.read_excel()`, `pd.read_sql()`, `df.to_csv()`, … |

---

## Column label rules

Column labels can be any hashable Python object — strings, integers, floats,
tuples, even `None`. In practice, stick to **simple unique strings**:

- **Dot access** (`df.age`) only works for string labels that are valid Python
  identifiers — no spaces, no leading digits, no collision with DataFrame
  attributes like `shape`, `index`, or `values`.
- **Bracket access** always works: `df["first name"]`, `df[2020]`.
- **Duplicate labels** are allowed but cause unpredictable behaviour in
  selection and many operations.

```python
df.my_col    # works if column name is "my_col"
df.2020      # SyntaxError
df.shape     # returns the DataFrame shape, NOT a "shape" column
```

---

## The row index cannot be removed

Every DataFrame has a row index — it cannot be dropped. Printing without it
requires `to_string(index=False)`.

The subject expects output like:

```
country 1800 1801 1802 1803 ... 2096 2097 2098 2099 2100
Afghanistan 28.2 28.2 28.2 28.2 ... 76.2 76.4 76.5 76.6 76.8
```

Constructing this trimmed preview takes four steps:

```python
left    = data.iloc[:, :5]        # first 5 columns
left["..."] = "..."               # append ellipsis column
right   = data.iloc[:, -5:]       # last 5 columns
trimmed = pd.concat([left, right], axis=1)
print(trimmed.to_string(index=False))
```
Latter on, i learnt about set_index(),

set_index() turns an existing column into the row index.

```python
df = pd.DataFrame({
    "country": ["Spain", "France", "Italy"],
    "population": [47, 67, 59]
})
```

Before:

```bash
   country  population
0    Spain          47
1   France          67
2    Italy          59
```

```python
df = df.set_index("country")
```
After:

```bash
         population
country
Spain            47
France           67
Italy            59
```

The "country" column is no longer a regular column — it's now the row label. This means you can do:
`df.loc["Spain"]` to  get Spain's row directly by name.

A few things to know:
By default it returns a new DataFrame (doesn't modify the original). 
Use inplace=True or reassign like above.

To undo it: df.reset_index() moves the index back into a regular column.

You can also set multiple columns as index: df.set_index(["country", "year"]) creates a MultiIndex.

---

## `pd.concat` — `axis` parameter

`axis` controls the direction of concatenation:

| `axis` | Effect |
|--------|--------|
| `0` (default) | Stack vertically — adds more **rows** |
| `1` | Join horizontally — adds more **columns** |

---

## `pd.read_csv` exceptions — parsing errors

Beyond filesystem errors (handled by `path_test`), `pd.read_csv` can raise:

| Exception | Cause |
|---|---|
| `pd.errors.EmptyDataError` | File is completely empty (zero bytes) |
| `pd.errors.ParserError` | File content cannot be parsed as CSV — malformed rows, inconsistent column count, bad delimiters |
| `UnicodeDecodeError` | File encoding does not match the default (UTF-8) |



[return](../../README.md)
