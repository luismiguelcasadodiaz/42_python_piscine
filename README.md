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