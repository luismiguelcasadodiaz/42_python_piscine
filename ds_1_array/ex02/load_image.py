import os
import numpy as np
from PIL import Image


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
    assert ext.lower() in (".jpg", ".jpeg"), \
        f"Expected a JPG/JPEG file, got '{ext[1:]}'"
    return abspath


def ft_load(path: str) -> np.ndarray:
    """Load a JPEG image from disk and return it as a NumPy array.

    Validates the given path using path_test, then opens the image with
    Pillow and converts it to a NumPy array. Prints the array's shape
    (height, width, channels) to stdout before returning.

    Args:
        path: A relative or absolute filesystem path to a JPEG image.

    Returns:
        A NumPy array of shape (height, width, channels) representing
        the pixel data of the image.

    Raises:
        AssertionError: If path validation fails (see path_test).
    """
    abspath = path_test(path)
    with Image.open(abspath) as im:
        arr = np.array(im, dtype = np.uint8)
        print(f"The shape of image is: {arr.shape}")
        return arr


def main():
    """Load and display landscape.jpg as a NumPy array."""
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()
