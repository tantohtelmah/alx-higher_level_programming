#!/usr/bin/python3
""" initialisation"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class wgich defines a Square"""
    
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        
    @property
    def size(self):
        """Getter for width."""
        
        return self.width

    @size.setter
    def size(self, value):
        """Setter for width."""
        
        self.width = self.validator("width", value)
        self.height = self.validator("width", value)


    @property
    def x(self):
        """Getter for x."""
        
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        
        self.__x = self.validator("x", value)

    @property
    def y(self):
        """Getter for y."""
        
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        
        self.__y = self.validator("y", value)
    
    def __str__(self):
        """Returns [Square] (<id>) 
        <x>/<y> - <square>
        """
        
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
        
    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""

        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
