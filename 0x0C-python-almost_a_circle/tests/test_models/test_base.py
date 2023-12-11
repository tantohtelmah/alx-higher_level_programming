#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_base(self):
        self.assertTrue(hasattr(Base, "__init__"))

if __name__ == '__main__':
    unittest.main()
