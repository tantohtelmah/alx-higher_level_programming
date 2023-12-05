#!/usr/bin/python3
""" initialisation """


def lookup(obj):
    """ the function"""

    return [attr for attr in dir(obj) if not callable(getattr(obj, attr))
            and attr.startswith("__")]
