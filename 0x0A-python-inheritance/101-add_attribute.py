#!/usr/bin/python3
""" adds a new attribute to an object """

def add_attribute(obj, name, value):
    if hasattr(obj, name):
        raise TypeError("can't add new attribute")
    else:
        obj.__setattr__(name, value)
