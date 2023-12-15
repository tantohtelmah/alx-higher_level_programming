import unittest
from models.square import Square
import json
import io

class TestSquare(unittest.TestCase):

    def test_square(self):
        self.assertTrue(hasattr(Square(5, 6, 6, 4), "__init__"))
   
    def setUp(self):
        self.square = Square(10, 20)
        
    def test_get_size(self):
        self.assertEqual(self.square.size, 10)

    def test_set_size(self):
        self.square.size = 15
        self.assertEqual(self.square.size, 15)

    def test_set_size_with_string(self):
        with self.assertRaises(TypeError):
            self.square.size = "10"

    def test_get_x(self):
        self.assertEqual(self.square.x, 20)

    def test_set_x(self):
        self.square.x = 5
        self.assertEqual(self.square.x, 5)

    def test_set_x_with_string(self):
        with self.assertRaises(TypeError):
            self.square.x = "0"

    def test_get_y(self):
        self.assertEqual(self.square.y, 0)

    def test_set_y(self):
        self.square.y = 10
        self.assertEqual(self.square.y, 10)

    def test_set_y_with_string(self):
        with self.assertRaises(TypeError):
            self.square.y = "0"
        
    def test_validator(self):
        # Test valid input
        sq = Square(1, 2, 4, 5)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 4)
        self.assertEqual(sq.id, 5)

        # Test invalid input
        with self.assertRaises(TypeError):
            sq.size = "invalid"
        with self.assertRaises(ValueError):
            sq.size = -1
        with self.assertRaises(ValueError):
            sq.size = 0
        

    def test_str(self):
        expected_output = "[Square] ({}) {}/{} - {}".format(self.square.id,
                                                                  self.square.x,
                                                                  self.square.y,
                                                                  self.square.size)
        self.assertEqual(str(self.square), expected_output)

    def test_update(self):
        self.square.update(89, 2, 4, 5)
        self.assertEqual(self.square.id, 89)
        self.assertEqual(self.square.size, 2)
        self.assertEqual(self.square.x, 4)
        self.assertEqual(self.square.y, 5)

    def test_to_dictionary(self):
        expected_output = {"id": self.square.id,
                           "size": self.square.size,
                           "x": self.square.x,
                           "y": self.square.y}
        self.assertEqual(self.square.to_dictionary(), expected_output)

    def test_save_to_file(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertEqual(json.loads(f.read()), [s1.to_dictionary(), s2.to_dictionary()])

if __name__ == '__main__':
    unittest.main()