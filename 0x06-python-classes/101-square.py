#!/usr/bin/python3
""" def of square class """


class Square:
    """ Implementation """
    print("i dey")
    def validator(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            return value

    def validatePos(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print("{}".format(" "* self.position[0]), end="")
                print("{}".format("#" * self.size))
    
    def __str__(self):
        return f"Sqaure({self.position})"
