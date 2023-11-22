#!/usr/bin/python3
""" def of square class """


class Square:
    """ Implementation """

    def validator(self, size):
        if type(size) is int:
            if size >= 0:
                return size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def __init__(self, size=0):
        self.__size = self.validator(size)

    def area(self):
        return self.__size * self.__size
