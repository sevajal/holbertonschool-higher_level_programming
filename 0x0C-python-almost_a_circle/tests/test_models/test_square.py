#!/usr/bin/python3

"""Unittest for almost a circle project"""

import unittest
from models.square import Square

class Test_square(unittest.TestCase):
    """Class Test for square models"""
    def test_square(self):
        self.assertTrue(True)

    def test_id(self):
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        s2 = Square(3, 1, 3, 12)
        self.assertEqual(s2.id, 12)

    def test_setters(self):
        self.assertRaises(TypeError, Square, ("2"))
        self.assertRaises(TypeError, Square, (10, 8, "3"))
