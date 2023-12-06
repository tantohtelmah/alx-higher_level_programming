#!/usr/bin/python3
"""initialisation"""


import json

def save_to_json_file(my_obj, filename):
    """ save to JSON file"""

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
