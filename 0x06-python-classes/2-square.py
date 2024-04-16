#!/usr/bin/python3
"""A class module"""


class Square:
    """A class Square that defines a square
    Attributes:
        size (int): The size of the square which is private
    """
    def __init__(self, size=0):
        """The __init__ method of the class square
        Note:
            Do not include the 'self' in the arguments
        Args:
            size (int): A private instance attribute
        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')
