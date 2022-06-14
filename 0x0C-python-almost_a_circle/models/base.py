#!/usr/bin/python3

"""Class Base"""


from fileinput import filename
import json
import os.path
from unittest import result


class Base:
    """This class will be the “base” of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """__init___ constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that returns the JSON string representation of
        list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that writes the JSON string representation of
        list_objs to a file"""
        my_list = []
        if list_objs is None:
            return my_list
        filename = cls.__name__ + ".json"
        my_list = [item.to_dictionary() for item in list_objs]
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """Method that returns the list of the JSON string representation
        json_string"""
        if json_string is None or json_string == []:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Method that returns an instance with all attributes already set"""
        obj1 = cls(1, 1, 0, 0)
        obj1.update(**dictionary)
        return obj1

    @classmethod
    def load_from_file(cls):
        """Method that returns a list of instances"""
        filename = cls.__name__ + ".json"
        if os.path.exists(filename) is False:
            return "[]"
        with open(filename, mode="r", encoding="utf-8") as file:
            my_lists = file.read()
            my_json_lists = cls.from_json_string(my_lists)
            for obj in my_json_lists:
                cls.create(**obj)
