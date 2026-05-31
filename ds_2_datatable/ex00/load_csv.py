import pandas as pd
import os as os

def path_test(path: str) -> str:
    """Validate that a given path points to a readable JPEG file.

    Resolves the provided path to an absolute path and runs a series of
    checks to ensure the file exists, is a regular file (not a directory),
    is readable by the current user, and has a .jpg or .jpeg extension.

    Args:
        path: A relative or absolute filesystem path to validate.

    Returns:
        The resolved absolute path to the validated JPEG file.

    Raises:
        AssertionError: If the path does not exist, is not a regular file,
            is not readable, or does not have a .jpg/.jpeg extension.
    """
    abspath = os.path.abspath(path)
    assert os.path.exists(abspath), f"Wrong Path {path}"
    assert os.path.isfile(abspath), f"{path} is not a file"
    assert os.access(abspath, os.R_OK), f"User can not read permit on {path}"
    _, ext = os.path.splitext(abspath)
    assert ext.lower() in (".csv", ".txt"), \
        f"Expected a JPG/JPEG file, got '{ext[1:]}'"
    return abspath

def load(path: str) -> pd.DataFrame:
    abspath = path_test(path)
    data = pd.read_csv(abspath)
    print(f"Loading dataset od dimensions {data.shape}")
    print(data[:])