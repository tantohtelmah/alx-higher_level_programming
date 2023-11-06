#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        if i <= len(my_list):
            print("{}".format(my_list[i - 1]))
        else:
            print("Index out of range")
