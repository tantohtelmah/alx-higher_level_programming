#!/usr/bin/python3
""" base """


import json


class Base:
    """Defines a Base class with private class attribute
    __nb_objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiates a Base object with id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file"""

        filename = cls.__name__ + ".json"
        obj_list = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(obj_list)
        with open(filename, "w", encoding="UTF8") as f:
            f.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                json_string = f.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle

        t = turtle.Turtle()
        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.setheading(0)
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)

        # Draw all the squares
        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            t.setheading(0)
            t.forward(square.width)
            t.left(90)
            t.forward(square.width)
            t.left(90)
            t.forward(square.width)
            t.left(90)
            t.forward(square.width)

        # Exit the turtle window
        turtle.done()
