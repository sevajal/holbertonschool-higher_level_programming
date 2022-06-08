#!/usr/bin/python3

"""Class Student"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """__init__ constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        my_dict = {}
        if hasattr(self, "__dict__"):
            my_dict = self.__dict__
        return my_dict
