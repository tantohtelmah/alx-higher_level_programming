#!/usr/bin/python3
class Rectangle:
    """
    initialisation

    """

    def __init__(self, width=0, height=0):
        """
        function
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """
        function
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        function
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @property
    def width(self):
        """
        function
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        function
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value
