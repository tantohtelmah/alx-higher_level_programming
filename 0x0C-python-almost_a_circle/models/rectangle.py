#!/usr/bin/python3
""" Rectangle """


from models.base import Base


class Rectangle(Base):
    """ Defines a rectangle that inherits from base"""

    def validator(self, input, value):
        """ Validates input"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(input))
        if input == "width" or input == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(input))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(input))
        return value

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialises a rectangle instance"""

        super().__init__(id)
        self.__width = self.validator("width", width)
        self.__height = self.validator("height", height)
        self.__x = self.validator("x", x)
        self.__y = self.validator("x", y)

    @property
    def width(self):
        """Getter for width."""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""

        self.__width = self.validator("width", value)

    @property
    def height(self):
        """Getter for height."""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""

        self.__height = self.validator("height", value)

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

    def area(self):
        """ Returns the area of the rectangle """

        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance with the character #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns [Rectangle] (<id>)
        <x>/<y> - <width>/<height>
        """
        a = {self.x}
        c = {self.y}
        b = {self.width}
        return f"[Rectangle]({self.id}) {a}/{c} - {b}/{self.height}"

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""

        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""

        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        obj_list = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(obj_list)
        with open(filename, "w") as f:
            f.write(json_str)
