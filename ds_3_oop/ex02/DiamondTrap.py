from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A royal character inheriting from both Baratheon and Lannister.

    Combines both houses through multiple inheritance. Due to Python's
    MRO (Method Resolution Order), Baratheon takes precedence, so the
    King inherits Baratheon's default traits (brown eyes, dark hair).
    Provides getters and setters to modify eye and hair color, allowing
    a King to override inherited family traits.

    Attributes:
        first_name: The character's first name.
        is_alive: Boolean indicating whether the character is alive.
        family_name: Inherited from Baratheon, set to "Baratheon".
        eyes: Eye color, initially "brown" (from Baratheon).
        hairs: Hair color, initially "dark" (from Baratheon).
    """

    def __init__(self, first_name: str = "", is_alive: bool = True):
        """Initialize a King character.

        Args:
            first_name: The character's first name. Defaults to an
                empty string.
            is_alive: Whether the character starts alive. Defaults
                to True.
        """
        super().__init__(first_name, is_alive)

    @property
    def eyes(self) -> str:
        """str: The King's eye color.

        Gets or sets the eye color. The value is stored in the
        private attribute ``_eyes``.
        """
        return self._eyes

    @eyes.setter
    def eyes(self, color: str):
        """Set the King's eye color.

        Args:
            color: The new eye color to assign.
        """
        self._eyes = color

    @property
    def hairs(self) -> str:
        """str: The King's hair color.

        Gets or sets the hair color. The value is stored in the
        private attribute ``_hairs``.
        """
        return self._hairs

    @hairs.setter
    def hairs(self, color: str) -> None:
        """Set the King's hair color.

        Args:
            color: The new hair color to assign.
        """
        self._hairs = color

    def get_eyes(self) -> str:
        """Return the King's eye color.

        Returns:
            A string representing the eye color.
        """
        return self.eyes

    def set_eyes(self, color: str) -> None:
        """Set the King's eyes color.

        Args:
            color: The new eyes color to assign.
        """
        self.eyes = color

    def get_hairs(self) -> str:
        """Return the King's hair color.

        Returns:
            A string representing the hair color.
        """
        return self.hairs

    def set_hairs(self, color: str) -> None:
        """Set the King's hair color.

        Args:
            color: The new hair color to assign.
        """
        self.hairs = color
