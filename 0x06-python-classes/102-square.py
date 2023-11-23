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

    def __init__(self, size=0):
        self.__size = self.validator(size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = self.validator(value)

    def area(self):
        return self.size * self.size
    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

