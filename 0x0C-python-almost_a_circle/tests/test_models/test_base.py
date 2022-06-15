#!/usr/bin/python3

"""Unittest for almost a circle project"""

import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle

class Test_base(unittest.TestCase):
    """Class Test for base models"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_base(self):
        self.assertTrue(True)
    
    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b4 = Base(12688)
        self.assertEqual(b4.id, 12688)
        b5 = Base(-15)
        self.assertEqual(b5.id, -15)
        b6 = Base(3.5)
        self.assertEqual(b6.id, 3.5)

    def test_to_json_string(self):
        output = io.StringIO()
        sys.stdout = output
        json_dictionary = Base.to_json_string(None)
        print(json_dictionary)
        self.assertEqual(output.getvalue(), "[]\n")

    def test_save_to_file(self):
        output = io.StringIO()
        sys.stdout = output
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            print(file.read())
        self.assertEqual(output.getvalue(), "[]\n")

    def test_from_json_string(self):
        output = io.StringIO()
        sys.stdout = output
        list_output = Rectangle.from_json_string(None)
        print("[{}] {}".format(type(list_output), list_output))
        self.assertEqual(output.getvalue(), "[<class 'list'>] []\n")

    def test_create(self):
        output = io.StringIO()
        sys.stdout = output
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        print(r2)
        self.assertEqual(output.getvalue(), "[Rectangle] (1) 1/0 - 3/5\n")

    def test_load_from_file(self):
        output = io.StringIO()
        sys.stdout = output
        list_rectangles_output = Rectangle.load_from_file()
        print(list_rectangles_output)
        self.assertEqual(output.getvalue(), "[]\n")

if __name__ == '__main__':
    unittest.main()