#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.
The size attribute is validated to ensure it is an integer and is
greater than or equal to 0.
"""


class Square:
    """
    Represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square, stored privately to ensure
                      controlled access and validation.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance with the specified size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
