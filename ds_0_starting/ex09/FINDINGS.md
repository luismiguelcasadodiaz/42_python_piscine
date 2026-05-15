# My First Package Creation — Findings

## Package structure

A **package** is a folder containing a special file `__init__.py`.
Each `.py` file inside the folder is a **module**.

```
ex09/
├── pyproject.toml          # build/install metadata
├── README.md               # package description
├── LICENSE                 # license file
└── ft_package/             # the package folder
    ├── __init__.py         # declares what the package exports
    ├── count_in_list.py    # module 1
    └── fraction_of_list.py # module 2
```

## `__init__.py` — the package public interface

`__init__.py` controls what is exported when someone does
`from ft_package import ...`. It uses **relative imports** (`.` prefix):

```python
# __init__.py
from .count_in_list import count_in_list
from .fraction_of_list import fraction_of_list
```

The `.` means "from the current package". Without `__init__.py` the folder
is just a directory — Python would not recognise it as a package.

## `pyproject.toml` — package metadata

The standard file that describes the package to `pip`, `build`, and `setuptools`:

```toml
[build-system]
requires = ["setuptools >= 77.0.3"]
build-backend = "setuptools.build_meta"

[project]
name = "ft_package"
version = "0.0.1"
description = "A short description"
readme = "README.md"
requires-python = ">=3.10"
license = "MIT"
authors = [
    {name = "Your Name", email = "you@example.com"}
]
dependencies = ["requests>=2.25"]
```

Key sections:
| Section | Purpose |
|---------|---------|
| `[build-system]` | Which tool builds the package |
| `[project]` | Name, version, description, authors, dependencies |
| `[project.urls]` | Homepage, repository links |

## Building and installing

All commands run from the folder containing `pyproject.toml`:

| Command | Effect |
|---------|--------|
| `pip install .` | Build and install directly |
| `pip install -e .` | Editable install — changes take effect without reinstalling |
| `python -m build` | Produce distributable files in `dist/` |
| `pip install ./dist/ft_package-0.0.1-py3-none-any.whl` | Install from wheel |
| `pip list` | Show installed packages |
| `pip show -v ft_package` | Show package details |

## Distribution formats

`python -m build` produces two files in `dist/`:

| File | Type | Description |
|------|------|-------------|
| `ft_package-0.0.1.tar.gz` | sdist | Source distribution — raw source code |
| `ft_package-0.0.1-py3-none-any.whl` | wheel | Built distribution — ready to install |

The wheel (`.whl`) is preferred for installation — faster, no build step needed.

## Editable mode — development workflow

```bash
pip install -e .
```

The `-e` flag installs the package as a symlink to your source folder.
Any code changes are immediately reflected without reinstalling.
Essential for iterative development.

## Publishing to PyPI / TestPyPI

TestPyPI (`test.pypi.org`) is a sandbox for testing uploads before going public:

```bash
twine upload --repository testpypi dist/*
```

Anyone can then install it from TestPyPI:
```bash
pip install --index-url https://test.pypi.org/simple/ ft_package
```

For the real PyPI, just `twine upload dist/*`.

## Relative imports with `.` prefix

Inside a package, modules import from each other using relative paths:

```python
from .count_in_list import count_in_list   # same package
from ..other_package import something      # parent package
```

Relative imports make the package self-contained — they work regardless of
where the package is installed.

## `list[str]` type hint syntax

Python 3.10+ allows built-in generics directly as type hints:

```python
def count_in_list(data: list[str], target: str) -> int:
```

Before 3.10 you needed `from typing import List` and `List[str]`.
This is why the subject requires `python >= 3.10`.



[return](../../README.md)
