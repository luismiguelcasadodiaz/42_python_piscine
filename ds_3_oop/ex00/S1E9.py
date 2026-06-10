from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class representing a character with name and alive status.

    Provides common functionality for all character types, including
    health management and alive-status checking. Subclasses must implement
    the ``die`` method.

    Attributes:
        first_name: The character's first name.
        is_alive: Boolean indicating whether the character is alive.
            Defaults to True.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Character instance.

        Args:
            first_name: The character's first name.
            is_alive: Whether the character starts alive. Defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def change_health(self):
        """Set the character's status to dead.

        Sets ``is_alive`` to False if the character is currently alive.
        Has no effect if already dead.
        """
        if self.is_alive:
            self.is_alive = False

    @abstractmethod
    def die(self):
        """Handle the character's death.

        Must be implemented by subclasses to define specific death behavior.
        """
        pass


class Stark(Character):
    """A character of House Stark, inheriting from Character.

    Implements the ``die`` method defined by the ``Character`` abstract
    base class. A Stark can only die once — calling ``die`` on an
    already dead character has no effect.

    The constructor is inherited from ``Character`` and accepts the
    same parameters (``first_name``, ``is_alive``).

    Attributes:
        first_name: The character's first name.
        is_alive: Boolean indicating whether the character is alive.
    """

    def die(self):
        """Set the character's status to dead if currently alive.

        Checks the ``is_alive`` attribute and toggles it through
        ``change_health`` only if the character is still alive.
        Has no effect if the character is already dead.
        """
        if self.is_alive:
            self.change_health()
