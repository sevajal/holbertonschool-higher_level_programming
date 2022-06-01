#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class Test for max_integer([..])"""
    def test_max_integer(self):
        """Test for correct results"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([4, -8, 0, 1]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([4, -8, 0, 1.54]), 4)
        self.assertEqual(max_integer("holaz"), "z")
        self.assertEqual(max_integer("HOLa"), "a")
        self.assertEqual(max_integer(["ha", "he", "hi", "ho", "hu"]), "hu")
        self.assertEqual(max_integer([[1], [2], [3]]), [3])
        self.assertEqual(max_integer([["a"], ["b"], ["c"]]), ["c"])
        self.assertEqual(max_integer(), None)

    def test_type(self):
        """Test for wrong types"""
        self.assertRaises(TypeError, max_integer, [1, 3, "5"])
        self.assertRaises(TypeError, max_integer, [1, 100, "h"])
        self.assertRaises(TypeError, max_integer, [1, 3, [5, 7]])
