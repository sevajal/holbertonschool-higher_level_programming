#!/usr/bin/python3

"""Unittest for almost a circle project"""

import unittest
from models.rectangle import Rectangle

class Test_rectangle(unittest.TestCase):
    """Class Test for rectangle models"""
    def test_rectangle(self):
        self.assertTrue(True)

    def test_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.id, 12)

    def test_setters(self):
        self.assertRaises(TypeError, Rectangle, (10, "2"))
        self.assertRaises(TypeError, Rectangle, (10, 8, "3"))
        """self.assertRaises(ValueError, Rectangle, (10, 10, 4, -5))
        self.assertRaises(ValueError, Rectangle, (-10, 10))"""
