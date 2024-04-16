#!/usr/bin/python3
"""A class module"""


class Square:
    """A class Square that define a square
    """
    def __init__(self, size=0):
        """The __init__ instance method
        Args:
            size (int): A private instance attribute that define
the size of the square
        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')
        elif self.__size <= 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """A public instance method that return square area
        """
        return self.__size ** 2
