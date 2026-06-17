# 42_python_piscine
Introductory Python curse

## starting

The overall aim in one sentence:

Take a complete beginner from "Hello World" to writing well-structured, PEP8-compliant Python programs that can
  be packaged, distributed, and measured against production-quality libraries — covering the full lifecycle of Python
   code.

+  Foundation — Python basics (ex00–ex03)                                                                             
  Learn the language's core data structures (list, tuple, set, dict), their mutability rules, how to use modules, and
   how Python represents "nothing" (None, NaN, 0, "", False).                                                        
                  
+  Input and control flow (ex04–ex05)
  Read from CLI and stdin, validate with assert, handle exceptions with EAFP, write properly structured standalone
  programs with main(), docstrings, and PEP8/flake8.

+  Functional programming tools (ex06)
  List comprehensions, lambda, filter(), iterators, lazy evaluation — the building blocks of data pipeline thinking.

+  Data structures as architecture (ex07)
  Use a dictionary as a lookup table instead of branching logic — an early lesson in choosing the right structure for
   the problem.

+  Generators and terminal I/O (ex08)
  yield, lazy sequences, live terminal output with \r/flush — and benchmarking your own code against a production
  library.

+  Packaging and distribution (ex09)
  Turn your code into an installable package with pyproject.toml, __init__.py, build tools, and the full PyPI
  workflow.

 


| File | Description | Findings |
|------|-------------|----------|
| Hello.py | Mutability of standard data structures: list, tuple, set, dict | [FINDINGS.md](ds_0_starting/ex00/FINDINGS.md) |
| format_ft_time.py | Exploring the `time` module members using `dir()` | [FINDINGS.md](ds_0_starting/ex01/FINDINGS.md) |
| find_ft_type.py | Type introspection with `__class__.__name__`, modules, if/elif/else, `in` operator | [FINDINGS.md](ds_0_starting/ex02/FINDINGS.md) |
| NULL_not_found.py | Scalar/null-like types: None, NaN, 0, "", False — IEEE 754 NaN behavior | [FINDINGS.md](ds_0_starting/ex03/FINDINGS.md) |
| whatis.py | CLI args with `sys.argv`, `assert`, EAFP try/except, exception chaining, modulo | [FINDINGS.md](ds_0_starting/ex04/FINDINGS.md) |
| building.py | String classification methods, `sys.stdin.read()`, `__main__` guard, docstrings, flake8 | [FINDINGS.md](ds_0_starting/ex05/FINDINGS.md) |
| ft_filter.py, filterstring.py | Iterators, list comprehensions, lambda, `filter()`, `split()`/`join()`, reimplementing built-ins | [FINDINGS.md](ds_0_starting/ex06/FINDINGS.md) |
| sos.py | Dictionary as O(1) lookup table, `all()`, generator expressions, `print(end=)`, input normalisation | [FINDINGS.md](ds_0_starting/ex07/FINDINGS.md) |
| Loading.py | `yield`/generators, `enumerate()`, `\r` terminal control, `flush=True`, time estimation, dynamic f-strings | [FINDINGS.md](ds_0_starting/ex08/FINDINGS.md) |
| ft_package/ | Package structure, `__init__.py`, `pyproject.toml`, build/install/publish workflow, relative imports | [FINDINGS.md](ds_0_starting/ex09/FINDINGS.md) |

## array

The overall aim in one sentence:

  + The module's aim is to replace the Python-list way of thinking with the NumPy-array way of thinking — learning
  vectorised operations, multi-dimensional indexing, and applying those skills to real image data.

  + Arrays and numerical computation
  Introduction to NumPy — the foundational library for data science. Python lists are not suited for numerical work
  (slow, no vectorised operations). NumPy arrays are the standard replacement. The module teaches you to think in
  arrays rather than loops.

  + Array manipulations
  Slicing, reshaping, transposing, broadcasting, applying operations across entire arrays at once — the core NumPy
  vocabulary that every data science library builds on.

  + Working on images
  Images are just 2D or 3D arrays of pixel values (height × width × channels). This bridges the gap between abstract
  array operations and something concrete and visual — rotating, cropping, colour channel manipulation, all done as
  array operations.

  + Specific rules introduced
  The same structural rules from ds_0 carry over: main() guard, no global scope, docstrings, flake8. But now the
  allowed functions shift from sys to numpy or any table manipulation library.




| File | Description | Findings |
|------|-------------|----------|
| give_bmi.py | NumPy arrays, dtype hierarchy, `np.issubdtype()`, `np.all()`, `np.finfo()`, `isinstance`, pytest | [FINDINGS.md](ds_1_array/ex00/FINDINGS.md) |
| array2D.py | 2D arrays, `.shape`, row-wise slicing, negative indices, slice clamping, bool guard, `.tolist()` | [FINDINGS.md](ds_1_array/ex01/FINDINGS.md) |
| load_image.py | Images as 3D `uint8` arrays, PIL/Pillow, `with` context, `os.path.abspath()`, `np.asarray()` | [FINDINGS.md](ds_1_array/ex02/FINDINGS.md) |
| zoom.py | crop/resize/zoom distinction, multi-axis slicing, PIL vs NumPy coord order, `convert("L")`, `np.newaxis`, matplotlib `cmap='gray'` trap, PIL canvas with custom axes | [FINDINGS.md](ds_1_array/ex03/FINDINGS.md) |
| rotate.py | 90° CCW rotation index remapping, shape swap on rotation, `np.zeros` float64 trap, `arr[y,x]` vs `arr[y][x]` | [FINDINGS.md](ds_1_array/ex04/FINDINGS.md) |
| pimp_image.py | `.copy()` vs assignment, channel isolation `arr[:,:,n]`, inversion broadcast, luminance dot product, `astype()`, `plt.subplots`, `axes.flat`, `cmap='gray'` | [FINDINGS.md](ds_1_array/ex05/FINDINGS.md) |

## tables
This module aims to teach me :
Pandas I/O + wide-format data + row filtering + transpose + line/scatter plots + log scale +
  DataFrame merging + correlation intuition.

+   Data structure — wide format                                                                                       
  The Gapminder CSVs are in wide format: rows = countries, columns = years. This is the opposite of the "tidy" long  
  format pandas prefers for plotting. Every exercise forces you to deal with this — selecting a row by country name, 
  then transposing .T to get years on the x-axis.                                                                    
                  
+ ex00 — CSV loading and error handling
  pd.read_csv(), .shape to print dimensions, and returning None gracefully for bad paths or bad formats. First
  contact with the DataFrame object.

+ ex01 — Row selection and line plot
  Filtering a single country row from a wide DataFrame, transposing it to a Series with year as index, then plotting.
   Teaches plt.title(), plt.xlabel(), plt.ylabel().

+ ex02 — Multi-series plot and legend
  Overlaying two countries on the same axes — teaches that each .plot() or plt.plot() call adds a new series to the
  current figure, and that plt.legend() is needed to distinguish them.

+ ex03 — Joining two DataFrames + scatter plot + log scale
  This is the richest exercise. Three distinct new concepts:
  - Merging two DataFrames (GDP and life expectancy) on the country column for a specific year
  - Scatter plot (plt.scatter()) instead of a line chart
  - Log scale on x-axis — plt.xscale('log') — because GDP spans orders of magnitude (300 to 10k), and the subject
  hint "Do you see a correlation?" introduces the concept of visualising correlation

  So the full picture: Pandas I/O + wide-format data + row filtering + transpose + line/scatter plots + log scale +
  DataFrame merging + correlation intuition.


| File | Description | Findings |
|------|-------------|----------|
| load_csv.py | DataFrame structure, column label rules, row index, `pd.concat` axis, `pd.read_csv` exceptions, trimmed preview with `iloc` + ellipsis column | [FINDINGS.md](ds_2_datatable/ex00/FINDINGS.md) |
| all_life.py | `set_index()`, `.loc` vs boolean mask, row→Series implicit transpose, column dtype trap, `astype(int)`, `MaxNLocator`, line plot anatomy | [FINDINGS.md](ds_2_datatable/ex01/FINDINGS.md) |
| aff_pop.py | column range slicing, `get_loc()`, `iloc` vs `loc`, `loc[x]`→Series vs `loc[[x]]`→DataFrame, cumulative plot state, `plt.legend()`, `FuncFormatter`, suffix parsing, `_` in numeric literals | [FINDINGS.md](ds_2_datatable/ex02/FINDINGS.md) |
| projection_life.py | `pd.merge()`, join semantics, duplicate column suffixes, Series `.rename()` before merge, `dropna()`, scatter plot, log scale, correlation intuition | [FINDINGS.md](ds_2_datatable/ex03/FINDINGS.md) |


## oop

 Here is what you will learn across the 5 exercises, from a concepts perspective:

+  ex00 — Abstract classes and basic inheritance
  You will learn what an abstract class is: a class that defines a contract (a method that must be implemented) but
  cannot be instantiated directly. You will learn how a child class inherits from it, satisfying that contract, and
  how instance attributes and methods work together to represent an object's state.

+  ex01 — Subclass hierarchies, string representation, and class methods
  You will learn how to build multiple sibling classes from the same parent, how to control how an object presents
  itself as a string (the difference between a human-readable and an unambiguous representation), and how to define
  alternative ways to construct objects at the class level rather than the instance level.

+  ex02 — Multiple inheritance and the diamond problem
  You will learn what happens when a class inherits from two parents that share a common ancestor (the diamond
  problem), how the language resolves method lookup order in that situation, and how to control read/write access to
  attributes through properties instead of exposing them directly.

+  ex03 — Operator overloading
  You will learn how to make your own classes respond to standard arithmetic operators, so that the natural syntax of
  the language (e.g. object + 5) triggers your own logic. This is the concept of giving objects behavior that
  mirrors built-in types.

+  ex04 — Static methods
  You will learn how to attach utility functions to a class without requiring an instance to be created first, and
  how decorators are used to change the nature of a method.

+  Running thread across all exercises: you will also practice writing proper documentation for every class and
  method, structuring programs with a main function, and keeping all logic out of the global scope — habits that
  distinguish professional code from scripts.

| File | Description | Findings |
|------|-------------|----------|
| S1E9.py | Abstract base class, `@abstractmethod` contract, single inheritance, `__dict__`, duck typing vs. ABC | [Findings.md](ds_3_oop/ex00/Findings.md) |
| S1E7.py | Sibling subclasses, `super().__init__()` extension, `__str__` vs `__repr__`, `eval(repr(obj))` convention, `@classmethod` factory method | [Findings.md](ds_3_oop/ex01/Findings.md) |
| DiamondTrap.py | Multiple inheritance, diamond problem, MRO, C3 linearization, `@property` with private backing store, cooperative `super()` chaining | [Findings.md](ds_3_oop/ex02/Findings.md) |
| ft_calculator.py | Operator overloading, element-wise vectorised ops, side-effect dunder methods, selective error handling, mutable default argument pitfall | [Findings.md](ds_3_oop/ex03/Findings.md) |
| ft_calculator.py | `@staticmethod`, class as namespace, vector-vector ops (dot product, add, subtract), `@staticmethod` vs `@classmethod` | [Findings.md](ds_3_oop/ex04/Findings.md) |


## Data Oriented Design

+  ex00 — *args and **kwargs with dynamic dispatch
  A single function accepts an unknown number of positional values and an unknown number of keyword arguments. The
  keyword argument values (not names) determine which statistical computation to run. You learn how to write truly
  variadic functions and how to use **kwargs as a dispatch table rather than a fixed parameter list. Error handling
  is required for unknown keywords and missing data.

+  ex01 — Closures and functions as first-class objects
  outer(x, function) returns an inner function that, each time it is called, applies function to the result of the
  previous call — building up a chain. The state (how many times it has been called, the current accumulated value)
  lives in the closure, not in a global variable (which is explicitly forbidden). You learn that functions can be
  passed as arguments, returned as values, and can carry private state through their enclosing scope.

+  ex02 — Writing a decorator factory
  callLimit(limit) returns a decorator, which returns a wrapper — three levels of nesting. The call counter lives in
  the closure. You go from using decorators (ex03 and ex04 of ds_3) to writing one from scratch, including the
  factory pattern where the decorator itself takes a configuration argument.

+  ex03 — Dataclasses
  @dataclass auto-generates __init__, __repr__, and __eq__ from field declarations. You learn how to mark fields as
  non-initializable (so passing them raises a TypeError), how to set computed defaults that run after construction,
  and when @dataclass is the right tool instead of a hand-written class.

  Running thread: functional programming patterns — closures, higher-order functions, and decorators — contrast
  directly with the OOP approach of ds_3. The module asks: what if state and behaviour live in functions rather than
  objects?

| File | Description | Findings |
|------|-------------|----------|
| statistics.py | `*args`/`**kwargs`, dispatcher pattern, functions as first-class objects, statistical formulas from scratch, `sorted()` on tuples, module docstrings, `typing.Any` | [Findings.md](ds_4_dod/ex00/Findings.md) |
