#!/usr/bin/python3
class Square:
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