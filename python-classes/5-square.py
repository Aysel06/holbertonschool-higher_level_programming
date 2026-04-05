#!/usr/bin/python3
"""This module defines a Square class with private size, getter/setter,
area calculation, and printing with '#' character.
"""


class Square:
    """A class that defines a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize th square with a size, using the setter for validation"""
        self.size = size  # Call setter for validation

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the '#' character in stdout."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print('#' * self.__size)
