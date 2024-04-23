#!/usr/bin/python3
"""Module that contains A class name square"""


class Square:
    """A class that allow to define a square"""
    def __init__(self, size=0):
        """A function that allows to initialize the private
        instance attribute size
        args:
            size (int) : the size of the square
        """
        self.__size = size

    def area(self):
        """A public instance method that give the area
        of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """A function that allow to retrieve the square's
        size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """A function that allows to set the size of square
        Args:
            value (int) : allow to set the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """A public instance method that allow to print
        in stdout the square with the character #
        """
        if self.size == 0:
            print("")
        for i in range(self.size):
            print("#" * self.size)
