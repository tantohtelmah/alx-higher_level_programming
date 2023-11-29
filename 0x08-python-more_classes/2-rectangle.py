#!/usr/bin/python3
class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
    - `width` (int): The width of the rectangle.
    - `height` (int): The height of the rectangle.
    """
    
    def width_validator(self, value):
        """
        Computes the area of the rectangle.

        Returns:
        - `int`: The area of the rectangle.
        """
        if type(value) is int:
            if value >= 0:
                return value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
    def height_validator(self, value):
        """
        Computes the area of the rectangle.

        Returns:
        - `int`: The area of the rectangle.
        """
        if type(value) is int:
            if value >= 0:
                return value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
            
    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the `Rectangle` class.

        Parameters:
        - `width` (int): The width of the rectangle.
        - `height` (int): The height of the rectangle.
        """
        self.__width = self.width_validator(width)
        self.__height = self.height_validator(height)
        
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        
    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
        - `int`: The area of the rectangle.
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Computes the perimeter of the rectangle.

        Returns:
        - `int`: The perimeter of the rectangle.
        """
        if self.width==0 or self.height==0:
            return 0
        return (2 * (self.width + self.height))
