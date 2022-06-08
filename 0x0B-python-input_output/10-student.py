#!/usr/bin/python3

"""Class Student"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """__init__ constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        my_dict = self.__dict__
        if type(attrs) is list and all(type(item) is str for item in attrs):
            my_other_dict = {}
            for key in my_dict:
                for attr in attrs:
                    if key == attr:
                        my_other_dict[attr] = my_dict.get(key)
            return my_other_dict
        else:
            return my_dict
