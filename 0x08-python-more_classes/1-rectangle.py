#!/usr/bin/python3
""" Initialisation """


class Rectangle:
    """ A class representing a rectangle. """

    def validator(self, value, attr):
        """ Validates the arguments """
        if type(value) is int:
            if value >= 0:
                return value
            else:
                raise ValueError("{} must be >= 0".format(attr))
        else:
            raise TypeError("{} must be an integer".format(attr))

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the `Rectangle` class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = self.validator(width, "width")
        self.__height = self.validator(height, "height")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = self.validator(value, "width")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = self.validator(value, "height")
