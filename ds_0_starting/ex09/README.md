# ft_package

A lightweight Python utility package for counting and analyzing occurrences of elements in lists.

## Installation
From current directory execute 
```bash
pip install .
```

## Functions

### `count_in_list(data, target)`

Counts the number of times `target` appears in `data`.

**Parameters:**
- `data` (`list[str]`): The list to search through.
- `target` (`str`): The element to count.

**Returns:** `int` — number of occurrences.

**Example:**
```python
from ft_package import count_in_list

fruits = ["apple", "banana", "apple", "cherry", "apple"]
count_in_list(fruits, "apple")  # → 3
```

---

### `fraction_of_list(data, target)`

Calculates the relative frequency (fraction) of `target` in `data`.

**Parameters:**
- `data` (`list[str]`): The list to search through.
- `target` (`str`): The element to measure.

**Returns:** `float` — fraction of elements equal to `target` (between 0.0 and 1.0).

**Example:**
```python
from ft_package import fraction_of_list

fruits = ["apple", "banana", "apple", "cherry", "apple"]
fraction_of_list(fruits, "apple")  # → 0.6
```

## Usage

```python
from ft_package import count_in_list, fraction_of_list

data = ["yes", "no", "yes", "yes", "no"]

print(count_in_list(data, "yes"))     # 3
print(fraction_of_list(data, "yes"))  # 0.6
```

## Notes

- Both functions iterate over the list once, making them O(n).
- `fraction_of_list` will raise a `ZeroDivisionError` if `data` is empty.
- Elements are compared using equality (`==`), so comparisons are case-sensitive.

## License

MIT