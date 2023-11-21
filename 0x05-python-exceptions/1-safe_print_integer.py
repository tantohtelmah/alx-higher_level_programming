#!/usr/bin/python3
def safe_print_integer(value):
        try:
            print("{}".format(int(value)), end="\n")
            return True
        except:
            return False
    