#!/usr/bin/python3
"""
initialisation
"""


class Student:
    """ Class Student"""

    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def class_to_json(self):
        """Returns the dictionary
            description with simple data structure
            (list, dictionary, string, integer and boolean)
            for JSON serialization of an object.
        """
        return self.__dict__
