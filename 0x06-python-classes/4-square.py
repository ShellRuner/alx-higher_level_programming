#!/usr/bin/python3
"""Module that contain a Square class"""


class Square:
    """A class that allow to define the size and area of square
    """
    def __init__(self, size=0):
        """Function that allow to initialize the
        private instance attribute "size"

        Args:
            size (int) : the size of the square
        """
        self.__size = size

#        if not isinstance(size, int):
#            raise TypeError("size must be an integer")
#        if size < 0:
#            raise ValueError("size must be >= 0")

    def area(self):
        """A public instance method that allows to
        calculate the square's area
        """
        return self.__size ** 2

    @property
    def size(self):
        """Property that allows to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """The setter that allows to set the size of the
        square
        Args:
            value (int) : allows to set the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
