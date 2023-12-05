#!/usr/bin/python3
""" Empty class """


class BaseGeometry:
    """ Base Geometry"""
    
    def area(self, width, height):
        return width * height
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value >= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ the rectangle class that inherits from BaseGeometry """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator(self.__width, self.__height)
        
    def __str__(self) -> str:
        return super().__str__()
    
class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        self.integer_validator(self.__size)
        
        def __str__(self) -> str:
            return super().__str__()