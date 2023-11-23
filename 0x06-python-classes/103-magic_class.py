#!/usr/bin/python3
import dis

""" class """


class MyClass:
    """ Implementation """

    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14159

    def circumference(self):
        return 2 * self.radius * 3.14159


dis.dis(MyClass.__init__)
