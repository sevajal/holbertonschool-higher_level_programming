#!/usr/bin/python3

"""Unittest for almost a circle project"""

import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle

class Test_rectangle(unittest.TestCase):
    """Class Test for rectangle models"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangle(self):
        self.assertTrue(True)

    def test_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.id, 12)

    def test_setters(self):
        self.assertRaises(TypeError, Rectangle, 10, "2")
        self.assertRaises(TypeError, Rectangle, 10, [2, 5])
        self.assertRaises(TypeError, Rectangle, 10, (2, 5))
        self.assertRaises(TypeError, Rectangle, 10.8, 2)
        self.assertRaises(TypeError, Rectangle, 10, 8, "3")
        self.assertRaises(TypeError, Rectangle, 10, 8, 3, 3.9)
        self.assertRaises(ValueError, Rectangle, 0, 8)
        self.assertRaises(ValueError, Rectangle, 10, -8)
        self.assertRaises(ValueError, Rectangle, 10, 8, 0, -2)
        r = Rectangle(1, 1)
        r.width = 10
        self.assertEqual(r.width, 10)
        r.height = 8
        self.assertEqual(r.height, 8)
        r.x = 3
        self.assertEqual(r.x, 3)
        r.y = 5
        self.assertEqual(r.y, 5)

    def test_area(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)
        r1 = Rectangle(5, 3)
        self.assertEqual(r1.area(), 15)

    def test_display(self):
        output = io.StringIO()
        sys.stdout = output
        Rectangle(2, 2).display()
        self.assertEqual(output.getvalue(), "##\n##\n")
        output = io.StringIO()
        sys.stdout = output
        Rectangle(2, 2, 1, 1).display()
        self.assertEqual(output.getvalue(), "\n ##\n ##\n")

    def test_str(self):
        output = io.StringIO()
        sys.stdout = output
        print(Rectangle(4, 6, 2, 1, 12))
        self.assertEqual(output.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")
        output = io.StringIO()
        sys.stdout = output
        print(Rectangle(5, 5, 1))
        self.assertEqual(output.getvalue(), "[Rectangle] (1) 1/0 - 5/5\n")

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 89)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 3)

    def test_to_dictionary(self):

        r1_dict = Rectangle(10, 2, 1, 9).to_dictionary()
        dic2 = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        for key, value in r1_dict.items():
            self.assertEqual(value, dic2[key])
        r1_dict = Rectangle(2, 4, 0, 0, 99).to_dictionary()
        dic2 = {'x': 0, 'y': 0, 'id': 99, 'height': 4, 'width': 2}
        for key, value in r1_dict.items():
            self.assertEqual(value, dic2[key])

if __name__ == '__main__':
    unittest.main()