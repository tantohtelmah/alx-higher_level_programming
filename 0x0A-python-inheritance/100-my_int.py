#!/usr/bin/python3
"""  inherits from int """


class MyInt(int):
    """ the class """
    
    def __eq__(self, other):
        """ function """
        
        return int(self) != int(other)

    def __ne__(self, other):
        """ function """
        return int(self) == int(other)
