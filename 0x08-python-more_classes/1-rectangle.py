#!/usr/bin/python3
class Rectangle:
    """ Initialising """
    
    
    def width_validator(self, value):
            if type(value) is int:
                if value >= 0:
                    return value
                else:
                    raise ValueError("width must be >= 0")
            else:
                raise TypeError("width must be an integer")
    def height_validator(self, value):
            if type(value) is int:
                if value >= 0:
                    return value
                else:
                    raise ValueError("height must be >= 0")
            else:
                raise TypeError("height must be an integer")
            
    def __init__(self, width=0, height=0):
        self.__width = self.width_validator(width)
        self.__height = self.height_validator(height)
        
        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            self.__width = self
            
        @property
        def height(self):
            return self.__height

        @height.setter
        def width(self, value):
            self.__height = self
