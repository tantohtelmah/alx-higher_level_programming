#!/usr/bin/python3
""" def of square class """


class Square:
    """ Implementation """

    def validator(self, value):
        if type(value) is int:
            if value >= 0:
                return value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def validatePos(self, value):
        if type(value) is tuple:
            if value[0] >= 0 and value[1] >= 0:
                return value
            else:
                raise TypeError("position must be a tuple of 2 \
                                positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def __init__(self, size=0, position=(0, 0)):
        self.__size = self.validator(size)
        self.__position = self.validatePos(position)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = self.validator(value)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = self.validatePos(value)

    def area(self):
        return self.size * self.size

    def my_print(self):
        for col in range(self.size):
            print(" " * self.position[0], self.size * "#", end="")
            print()
        if self.size == 0:
            print()
