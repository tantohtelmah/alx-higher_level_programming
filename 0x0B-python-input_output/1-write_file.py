#!/usr/bin/python3
"""initialisation"""


def write_file(filename="", text=""):
    """ Writes to a file"""

    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
