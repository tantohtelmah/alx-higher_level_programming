#!/usr/bin/python3
def safe_print_integer(value):
        try:
            print("{:d}".format(int(value)), end="\n")
            return True
        except ValueError:
            return False
    