#!/usr/bin/python3
"""Module that contains a class name square"""


class Square:
    """A class that allows to define a square"""
    def __init__(self, size=0, position=(0, 0)):
        """A function that allows to initialize attributes
        Args:
            size (int) : A private instance attribute and size
                         of the square
            position (int, int) : A private instance attribute
                                  and allows to coordinate the
                                  square
        """
        self.size = size
        self.position = position

    def area(self):
        """A public instance method that give the area of the
        square
        """
        return self.__size ** 2

    @property
    def size(self):
        """A function that allows to retrieve the square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """A function that allows to set the size
        Args: set  the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """A function that allows to retrieve the position of
        the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """A function that allows to set the square position
        Args:
            value (int, int) : set the position
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """A public instance method that allows to print
        in stdout the square with the character "#"
        """
        if self.__size == 0:
            print(" ")
        [print('') for _ in range(0, self.__position[1])]
        for _ in range(0, self.__size):
            [print(" ", end="") for _ in range(0, self.__position[0])]
            for _ in range(self.__size):
                print("#", end="")
            print()
