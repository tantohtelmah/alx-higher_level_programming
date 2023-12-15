import unittest
from models.rectangle import Rectangle
import json
import io
from contextlib import redirect_stdout

class TestRectangle(unittest.TestCase):
    """ tests for the rectangle"""
    def test_rectangle(self):
        self.assertTrue(hasattr(Rectangle(5, 6, 6, 4), "__init__"))
   
    def setUp(self):
        self.rectangle = Rectangle(10, 20)

    def test_get_width(self):
        self.assertEqual(self.rectangle.width, 10)

    def test_set_width(self):
        self.rectangle.width = 15
        self.assertEqual(self.rectangle.width, 15)

    def test_set_width_with_string(self):
        with self.assertRaises(TypeError):
            self.rectangle.width = "10"

    def test_get_height(self):
        self.assertEqual(self.rectangle.height, 20)

    def test_set_height(self):
        self.rectangle.height = 25
        self.assertEqual(self.rectangle.height, 25)

    def test_set_height_with_string(self):
        with self.assertRaises(TypeError):
            self.rectangle.height = "20"

    def test_get_x(self):
        self.assertEqual(self.rectangle.x, 0)

    def test_set_x(self):
        self.rectangle.x = 5
        self.assertEqual(self.rectangle.x, 5)

    def test_set_x_with_string(self):
        with self.assertRaises(TypeError):
            self.rectangle.x = "0"

    def test_get_y(self):
        self.assertEqual(self.rectangle.y, 0)

    def test_set_y(self):
        self.rectangle.y = 10
        self.assertEqual(self.rectangle.y, 10)

    def test_set_y_with_string(self):
        with self.assertRaises(TypeError):
            self.rectangle.y = "0"
        
    def test_validator(self):
        # Test valid input
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 5)

        # Test invalid input
        with self.assertRaises(TypeError):
            rect.width = "invalid"
        with self.assertRaises(ValueError):
            rect.width = -1
        with self.assertRaises(ValueError):
            rect.height = 0
        

    def test_area(self):
        """Tests the area of a rectangle"""

        width = 5
        height = 10
        rectangle = Rectangle(width, height)
        expected_area = width * height
        self.assertEqual(rectangle.area(), expected_area)

    def test_display(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.rectangle.display()
            output = buf.getvalue().strip()
        expected_output = "\n" * self.rectangle.y + \
                          ("\n".join([" " * self.rectangle.x + "#" * self.rectangle.width
                                      for i in range(self.rectangle.height)]))
        self.assertEqual(output, expected_output)

    def test_str(self):
        expected_output = "[Rectangle] ({}) {}/{} - {}/{}".format(self.rectangle.id,
                                                                  self.rectangle.x,
                                                                  self.rectangle.y,
                                                                  self.rectangle.width,
                                                                  self.rectangle.height)
        self.assertEqual(str(self.rectangle), expected_output)

    def test_update(self):
        self.rectangle.update(89, 2, 3, 4, 5)
        self.assertEqual(self.rectangle.id, 89)
        self.assertEqual(self.rectangle.width, 2)
        self.assertEqual(self.rectangle.height, 3)
        self.assertEqual(self.rectangle.x, 4)
        self.assertEqual(self.rectangle.y, 5)

    def test_to_dictionary(self):
        expected_output = {"id": self.rectangle.id,
                           "width": self.rectangle.width,
                           "height": self.rectangle.height,
                           "x": self.rectangle.x,
                           "y": self.rectangle.y}
        self.assertEqual(self.rectangle.to_dictionary(), expected_output)

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(json.loads(f.read()), [r1.to_dictionary(), r2.to_dictionary()])

if __name__ == '__main__':
    unittest.main()
