#!/usr/bin/python3
""" test cases for base"""


import unittest
from models.base import Base
import json


test_base_instance = Base()

class TestBase(unittest.TestCase):
    """ the test case class"""

    def test_base(self):
        self.assertTrue(hasattr(Base, "__init__"))

    def test_to_json_string(self):
        list_dictionaries ={
    "United States": "Washington D.C.",
    "Italy": "Rome",
    "England": "London"
    }
        list_dictionaries1 = None
        list_dictionaries2 = {}
        self.assertTrue(test_base_instance.to_json_string(list_dictionaries), json.dumps(list_dictionaries))
        self.assertTrue(test_base_instance.to_json_string(list_dictionaries1), [])
        self.assertTrue(test_base_instance.to_json_string(list_dictionaries2), [])

    def test_from_json_string(self):
        json_string = '[{"id": 1}, {"id": 2}, {"id": 3}]'
        obj_list = Base.from_json_string(json_string)
        self.assertEqual(len(obj_list), 3)
        self.assertEqual(obj_list[0]["id"], 1)
        self.assertEqual(obj_list[1]["id"], 2)
        self.assertEqual(obj_list[2]["id"], 3)

    # def test_save_to_file(self):
    #     objs = [Base(1), Base(2), Base(3)]
    #     Base.save_to_file(objs)
    #     filename = Base.__name__ + ".json"
    #     with open(filename, "r") as f:
    #         json_str = f.read()
    #         obj_list = Base.from_json_string(json_str)
    #     self.assertEqual(len(objs), len(obj_list))
    #     for i in range(len(objs)):
    #         self.assertEqual(objs[i].to_dictionary(), obj_list[i].to_dictionary())
    
    def test_create(self):
        """ tests for the create module"""

        dictionary = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        rect = test_base_instance.create(**dictionary)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)


    # def test_load_from_file(self):
    #     """ tests load from a file module"""

    #     filename = Base.__name__ + ".json"
    #     with open(filename, "w") as f:
    #         f.write('[{"id": 1}, {"id": 2}, {"id": 3}]')
    #     objs = Base.load_from_file()
    #     self.assertEqual(len(objs), 3)
    #     self.assertEqual(objs[0].id, 1)
    #     self.assertEqual(objs[1].id, 2)
    #     self.assertEqual(objs[2].id, 3)

if __name__ == '__main__':
    unittest.main()
