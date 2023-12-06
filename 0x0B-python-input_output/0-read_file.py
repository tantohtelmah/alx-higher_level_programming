#!/usr/bin/python3
""" initialisatio"""


def read_file(filename=""):
    """Reading a file"""

    with open(filename, encoding="utf-8") as f:
        print(f.read())
