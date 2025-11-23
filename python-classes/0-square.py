#!/usr/bin/python3
"""
Module: 0-square

This module defines the Square class, which represents a square
with a private size attribute. It allows instantiation of
Square objects with a specific size.
"""

class Square:
    """
    Class that defines a square by its size.

    Attributes:
        __size (int): The private size of the square.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
