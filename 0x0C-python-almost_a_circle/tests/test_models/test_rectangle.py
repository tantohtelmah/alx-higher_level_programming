import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_area(self):
        """Tests the area of a rectangle"""

        width = 5
        height = 10
        rectangle = Rectangle(width, height)
        expected_area = width * height
        self.assertEqual(rectangle.area(), expected_area)

if __name__ == '__main__':
    unittest.main()
