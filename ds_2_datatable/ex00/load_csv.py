import pandas as pd
import os


def path_test(path: str) -> str:
    """Validate that a given path points to a readable csv file.

    Resolves the provided path to an absolute path and runs a series of
    checks to ensure the file exists, is a regular file (not a directory),
    is readable by the current user, and has a .csv or .txt extension.

    Args:
        path: A relative or absolute filesystem path to validate.

    Returns:
        The resolved absolute path to the validated csv file.

    Raises:
        AssertionError: If the path does not exist, is not a regular file,
            is not readable, or does not have a .csv/.txt extension.
    """
    abspath = os.path.abspath(path)
    assert os.path.exists(abspath), f"Wrong Path {path}"
    assert os.path.isfile(abspath), f"{path} is not a file"
    assert os.access(abspath, os.R_OK), f"User can not read permit on {path}"
    _, ext = os.path.splitext(abspath)
    assert ext.lower() in (".csv", ".txt"), \
        f"Expected a csv/TXT file, got '{ext[1:]}'"
    return abspath


def load(path: str) -> pd.DataFrame | None:
    """Load a csv file, print its dimensions, and return a trimmed preview string.

    Resolves the file path via ``path_test``, reads the csv into a pandas
    DataFrame, and constructs a preview showing the first and last five
    columns with an ellipsis separator in between. The full dataset
    dimensions are printed before the preview is returned.

    Args:
        path: A string representing the path to the csv file. Passed to
            ``path_test`` for validation and resolution to an absolute path.

    Returns:
        A pandas DataFrame containig the parsev csv file or
        None if an error occurs during loading or parsing.

    Raises:
        AssertionError: If ``path_test`` fails validation (caught and printed).
        pd.errors.EmptyDataError: If the file is empty (caught and printed).
        pd.errors.ParserError: If the file cannot be parsed as csv (caught
            and printed).
        Exception: Any other unexpected error (caught and printed).

    Note:
        All exceptions are caught and printed rather than re-raised,
        causing the function to return None implicitly on failure.

    See Also:
        path_test: Validates and resolves the given file path.
    """
    try:
        abspath = path_test(path)
        data = pd.read_csv(abspath)
        print(f"Loading dataset of dimensions {data.shape}")
        left = data.iloc[:, :5]
        left["..."] = "..."
        righ = data.iloc[:, -5:]
        trimmed = pd.concat([left, righ], axis=1)
        print(trimmed.to_string(index=False))
        return data
    except AssertionError as e:
        print(e)
    except pd.errors.EmptyDataError:
        print("Empty file")
    except pd.errors.ParserError:
        print("Could not parse this csv file")
    except Exception as e:
        print(f"Unexpected error {e}")

def main():
    """Loas a file an partilly prints it"""
    load("life_expectancy_years.csv")


if __name__ == "__main__":
    main()
