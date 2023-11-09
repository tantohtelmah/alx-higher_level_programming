#!/usr/bin/python3
def common_elements(set_1, set_2):
    c_elements = []
    for i in set_1:
        if i in set_2:
            c_elements.append(i)
    return c_elements
