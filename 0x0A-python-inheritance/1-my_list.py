#!/usr/bin/python3
""" MyList class """


class MyList(list):
    """ Inherits from List"""
    
    
    def print_sorted(self):
        print(sorted(self))
