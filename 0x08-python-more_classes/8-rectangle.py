#!/usr/bin/python3
"""Module that contain a class Rectangle"""


class Rectangle:
    """An empty class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """A method that defines the width and the height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """allow to Calculate the area"""
        return self.width * self.height

    def perimeter(self):
        """Allows to calculate the perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):
        """The function that print the rectangle"""
        if self.width == 0 or self.height == 0:
            return ''
        rectangle = ""
        for i in range(self.height):
            rectangle += str(self.print_symbol) * self.width + "\n"
        return rectangle.rstrip()

    def __repr__(self):
        """The function return a string representation
        of the object
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """The method that print a message when an instance is
        deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
