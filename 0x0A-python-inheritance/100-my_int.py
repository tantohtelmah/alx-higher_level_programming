#!/usr/bin/python3
""" initialisation """


class MyInt(int):
    """ the class """

    def __eq__(self, other):
        """ function """

        return int(self) != int(other)

    def __ne__(self, other):
        """function"""

        return int(self) == int(other)
