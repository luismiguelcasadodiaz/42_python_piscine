"""Student data model with auto-generated login and ID.

Uses Python dataclasses to define a Student with automatic login
construction and random ID generation on instantiation.
"""

import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random 15-character lowercase alphabetic ID.

    Returns:
        A string of 15 random lowercase letters.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A student record with auto-generated login and unique ID.

    On creation, the login is built from the first letter of the
    name (uppercased) concatenated with the surname, and the ID
    is generated as a random 15-character string via ``generate_id``.

    Attributes:
        name: The student's first name.
        surname: The student's surname.
        active: Whether the student is currently active.
            Defaults to True.
        login: Auto-generated login string in the format
            ``"N" + surname`` (e.g., "Jdoe" for "John", "doe").
            Not settable via the constructor.
        id: A randomly generated 15-character alphabetic string.
            Not settable via the constructor.

    Example:
        >>> s = Student(name="John", surname="doe")
        >>> s.login
        'Jdoe'
        >>> len(s.id)
        15
    """
    name: str
    surname: str
    active: bool = field(init=False, default=True)
    login: str = field(init=False, default="")
    id: str = field(init=False, default="")

    def __post_init__(self):
        """Build the login and generate the ID after dataclass init.

        Constructs the login from the first character of ``name``
        (uppercased) and ``surname``. Generates a random ID via
        ``generate_id``.

        Note:
            If ``name`` is an empty string, an IndexError is caught
            and an error message is printed. In that case, ``login``
            and ``id`` remain as empty strings.
        """
        try:
            self.login = self.name[0].upper() + self.surname
            self.id = generate_id()
        except IndexError:
            print("Empty name not allowed")
