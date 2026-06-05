# Life Expectancy vs GDP — Findings

## `pd.merge()` — joining two DataFrames

`pd.merge()` combines two DataFrames on a common key column, like a SQL JOIN:

```python
df1 = pd.DataFrame({
    "country":    ["Spain", "France", "Italy"],
    "population": [47, 67, 59]
})
df2 = pd.DataFrame({
    "country": ["Spain", "France", "Germany"],
    "capital": ["Madrid", "Paris", "Berlin"]
})

result = pd.merge(df1, df2, on="country")
```

Result — only matching rows kept (inner join by default):
```
  country  population capital
    Spain          47  Madrid
   France          67   Paris
```

### The `how` parameter — join semantics

| `how` | Rows kept |
|-------|-----------|
| `"inner"` (default) | only rows matching in **both** DataFrames |
| `"left"` | all rows from the left DataFrame; NaN where right has no match |
| `"right"` | all rows from the right DataFrame; NaN where left has no match |
| `"outer"` | all rows from both; NaN wherever there is no match |

```python
pd.merge(df1, df2, on="country", how="outer")
#    country  population  capital
#      Spain        47.0   Madrid
#     France        67.0    Paris
#      Italy        59.0      NaN
#    Germany         NaN   Berlin
```

### Other merge options

```python
# Different key column names in each DataFrame
pd.merge(df1, df2, left_on="country_name", right_on="nation")

# Merge on multiple columns
pd.merge(df1, df2, on=["country", "year"])
```

The key column appears **once** in the result (not duplicated). All other
columns from both DataFrames are kept.

### Duplicate non-key column names

When both DataFrames have a non-key column with the same name, pandas appends
suffixes to distinguish them:

```python
pd.merge(df1, df2, on="country")
# columns: ["country", "value_x", "value_y"]

pd.merge(df1, df2, on="country", suffixes=("_pop", "_gdp"))
# columns: ["country", "value_pop", "value_gdp"]
```

`_x` comes from the left DataFrame, `_y` from the right.

---

## Series name — rename before merging

`income[year]` returns a Series whose name is the column label — e.g. `1900`
(an integer). After merging two such Series, the result has columns named
`1900_x` and `1900_y`. Column names starting with a digit cannot be accessed
via dot notation:

```python
plt.scatter(data.1900_x, data.1900_y)
#                ^ SyntaxError: invalid decimal literal
```

Rename each Series before merging so the resulting columns have valid
Python identifiers:

```python
income_year = income[year].dropna().rename("dolar")
life_year   = life[year].dropna().rename("life_exp")
data = pd.merge(income_year, life_year, on="country", how="inner")

plt.scatter(data.dolar, data.life_exp)   # dot access works
```

---

## `dropna()` — removing missing values

`dropna()` removes entries where a value is `NaN`. On a Series it drops NaN
elements; on a DataFrame the `how` and `axis` parameters control the behaviour:

```python
df.dropna()                            # drop row if ANY column has NaN (default)
df.dropna(how="all")                   # drop row only if ALL columns are NaN
df.dropna(subset=["income", "life"])   # only check these columns
df.dropna(axis=1)                      # drop COLUMNS that have any NaN
```

The default (`how="any"`, `axis=0`) is the strictest — a single NaN anywhere
in a row removes it. In this exercise, calling `.dropna()` on each Series
before the merge ensures the scatter has no gaps from countries with missing
data in either dataset.

---

## Scatter plot — `plt.scatter()`

Unlike `plt.plot()`, a scatter plot draws independent dots with no connecting
line. It is appropriate when observations are independent (countries, not time
steps) and you want to visualise the **relationship between two continuous
variables**:

```python
plt.scatter(data.dolar, data.life_exp)
```

---

## Log scale — `plt.xscale("log")`

GDP per capita spans several orders of magnitude (hundreds to tens of
thousands). On a linear scale, poor countries are compressed into a thin band
on the left and the correlation is hard to see. A log scale spreads them out:

```python
plt.xscale("log")
plt.gca().xaxis.set_major_formatter(
    plt.FuncFormatter(lambda v, p: f"{v/1_000:.0f}k"))
```

**Scale choice changes what a chart communicates** — the same data with a
linear x-axis looks like a weak correlation; with a log x-axis a clear
positive trend emerges.

---

## Correlation as a visual concept

The subject asks "Do you see a correlation between life span and gross domestic
product?" — the first explicit nudge toward statistical thinking. The scatter
plot reveals a positive trend: in 1900 wealthier countries (higher GDP per
capita) generally had longer life expectancy. The chart does not prove
causation, but it makes the relationship visible at a glance.



[return](../../README.md)
