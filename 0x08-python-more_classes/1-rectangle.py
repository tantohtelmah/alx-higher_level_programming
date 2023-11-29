#!/usr/bin/python3
class Rectangle:
    """
    This module provides a set of utility functions for working with strings.

    Functions:
    - `__init__(self, width, height)`: initialisation
    """

    def __init__(self, width=0, height=0):
        def __init__(self, width, height):
            """
            Initializes a new instance of the `Rectangle` class.

            Parameters:
            - `width` (int): The width of the rectangle.
            - `height` (int): The height of the rectangle.
            """
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value
