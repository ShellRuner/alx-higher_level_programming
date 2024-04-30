#!/usr/bin/python3
"""Module that contain a class Rectangle"""


class Rectangle:
    """An empty class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """A method that defines the width and the height"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """allows to retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """allows to set the height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @property
    def width(self):
        """allow to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value
