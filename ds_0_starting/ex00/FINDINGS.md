# Data Objects Mutability — Findings

## List — Mutable
Direct item assignment is supported.
```python
ft_list[1] = "World"  # OK
```

## Tuple — Immutable
Item assignment is **not** allowed. To "modify" a tuple, a new one must be created.
```python
ft_tuple[1] = "Spain"   # TypeError: 'tuple' object does not support item assignment
ft_tuple = ("Hello", "Spain")  # creates a new tuple
```

## Set — Mutable but unordered, no index assignment
Sets do not support item assignment via index. Elements are added/removed via methods.
```python
ft_set[0] = "Barcelona!"  # TypeError: 'set' object does not support item assignment
ft_set.add("Barcelona!")   # OK
ft_set.discard("tutu!")    # OK
```
The order elements appear when printed is **not** insertion order — it depends on each element's hash value.
```python
print(hash("Hello"))      # e.g.  1894580244085487633
print(hash("tutu!"))      # e.g. -2685032689226324145
print(hash("Barcelona!")) # e.g.  5765645633518783299
```

## Dict — Mutable
Key-value pairs can be updated directly.
```python
ft_dict["Hello"] = "42 Barcelona"  # OK
```

## Summary

| Type  | Mutable | Index assignment | Ordered |
|-------|---------|-----------------|---------|
| list  | yes     | yes             | yes     |
| tuple | no      | no              | yes     |
| set   | yes     | no              | no (hash-based) |
| dict  | yes     | by key          | yes (insertion order, Python 3.7+) |



[return](../../README.md)
