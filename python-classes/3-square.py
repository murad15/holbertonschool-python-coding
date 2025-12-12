#!/usr/bin/python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Represent a square defined by its size."""

    def __init__(self, size=0):
        """Initialize a Square instance with a given size."""
        self.__size = size

    @property
    def size(self):
        """Initialize a Square instance with a given size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Initialize a Square instance with a given size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
