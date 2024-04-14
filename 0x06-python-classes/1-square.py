#!/usr/bin/python3
"""A class Square that define a square"""


class Square:
    """A class that define a square by a Private size
    Attributes:
        size: A private instance attribute.
    """
    def __init__(self, size):
        """An __init__ method description
        Note:
            Do not include the 'self' param in the 'Args' section

        Args:
            size: The size of the square
        """
        self.__size = size
