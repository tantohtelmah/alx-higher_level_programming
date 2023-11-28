#!/usr/bin/python3
class Rectangle:
    pass
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
        self.__width = value
        
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        
    def area(self):
        return self.width * self.height
    def perimeter(self):
        if self.width==0 or self.height==0:
            return 0
        return (2 * (self.width + self.height))
    
    print_symbol = '#'
    number_of_instances = 0
    
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            self.print_symbol = ""
            for i in range(self.height):
                for j in range(self.width):
                    self.print_symbol += "#"
                self.print_symbol += "\n"
            return self.print_symbol

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
    
    def __del__(self):
        print("Bye rectangle...")
        
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if rect_1 is not isinstance(Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif rect_2 is not isinstance(Rectangle):
            raise TypeError("rec_2 must be an instance of Rectangle")
        else:
            
            