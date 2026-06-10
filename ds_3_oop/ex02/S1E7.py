from S1E9 import Character


class Baratheon(Character):
    """A character of House Baratheon, inheriting from Character.

    Initializes with the Baratheon family traits: brown eyes and dark
    hair. Implements the ``die`` method defined by the ``Character``
    abstract base class.

    Attributes:
        first_name: The character's first name.
        is_alive: Boolean indicating whether the character is alive.
        family_name: Always set to "Baratheon".
        eyes: Eye color, set to "brown".
        hairs: Hair color, set to "dark".
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Baratheon character.

        Args:
            first_name: The character's first name. The character
                starts alive by default via the parent constructor.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Set the character's status to dead if currently alive.

        Checks the ``is_alive`` attribute and toggles it through
        ``change_health`` only if the character is still alive.
        Has no effect if the character is already dead.
        """
        if self.is_alive:
            self.change_health()

    def __str__(self):
        """Return the informal string representation of the character.

        Delegates to ``__repr__`` to provide the same Vector-style
        tuple string for both ``str()`` and ``repr()`` calls.

        Returns:
            A string in the format:
            ``"Vector ('family_name', 'eyes', 'hairs')"``
        """
        return self.__repr__()

    def __repr__(self):
        """Return the formal string representation of the character.

        Formats the character's family name, eye color, and hair color
        as a Vector-style tuple string.

        Returns:
            A string in the format:
            ``"Vector ('family_name', 'eyes', 'hairs')"``
        """
        return f"Vector ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """A character of House Lannister, inheriting from Character.

    Initializes with the Lannister family traits: blue eyes and light
    hair. Implements the ``die`` method defined by the ``Character``
    abstract base class. Provides a class method factory for creating
    Lannister instances.

    Attributes:
        first_name: The character's first name.
        is_alive: Boolean indicating whether the character is alive.
        family_name: Always set to "Lannister".
        eyes: Eye color, set to "blue".
        hairs: Hair color, set to "light".
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Lannister character.

        Args:
            first_name: The character's first name.
            is_alive: Whether the character starts alive. Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Set the character's status to dead if currently alive.

        Checks the ``is_alive`` attribute and toggles it through
        ``change_health`` only if the character is still alive.
        Has no effect if the character is already dead.
        """
        if self.is_alive:
            self.change_health()

    def __str__(self):
        """Return the informal string representation of the character.

        Returns:
            None — this method is not implemented and falls back to
            the default ``object.__str__`` behavior.
        """
        return f"Vector ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return the formal string representation of the character.

        Formats the character's family name, eye color, and hair color
        as a Vector-style tuple string.

        Returns:
            A string in the format:
            ``"Vector ('family_name', 'eyes', 'hairs')"``
        """
        return f"Lannister('{self.first_name}', {self.is_alive})"

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool):
        """Create a new Lannister instance via a factory method.

        Provides an alternative constructor for creating Lannister
        characters. Supports subclasses through the use of ``cls``.

        Args:
            first_name: The character's first name.
            is_alive: Whether the character starts alive.

        Returns:
            A new instance of ``Lannister`` (or its subclass).
        """
        return cls(first_name, is_alive)
