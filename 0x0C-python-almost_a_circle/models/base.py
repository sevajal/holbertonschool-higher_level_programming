#!/usr/bin/python3

"""Class Base"""


import json


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
        """Method that returns the JSON string representation of list_dictionaries"""
        if list_dictionaries == None or list_dictionaries == {}:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            return "[]"
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string([item.to_dictionary() for item in list_objs]))
