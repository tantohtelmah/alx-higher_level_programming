#!/usr/bin/python3
""" initialisation"""


def append_write(filename="", text=""):
    """ appends at the end of a file"""

    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
