#!/usr/bin/python3
class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
    - `width` (int): The width of the rectangle.
    - `height` (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new instance of the `Rectangle` class.

        Parameters:
        - `width` (int): The width of the rectangle.
        - `height` (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
        - `int`: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Computes the perimeter of the rectangle.

        Returns:
        - `int`: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

