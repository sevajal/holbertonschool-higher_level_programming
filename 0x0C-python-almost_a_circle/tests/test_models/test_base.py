#!/usr/bin/python3

"""Unittest for almost a circle project"""

import unittest
from models.base import Base

class Test_base(unittest.TestCase):
    """Class Test for base models"""
    def test_base(self):
        self.assertTrue(True)
    
    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
