#!/usr/bin/python3

"""MagicClass program"""


class MagicClass:
    """Create a class called MagicClass"""
    def __init__(self, radius):
        """Constructor method __init___"""
        if radius is not int or radius is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Return the area of a circle"""
        return ((self.__radius ** 2) * math(pi))

    def circumference(self):
        """Return the circumference of a circle"""
        return (math(pi) * (self.__radius ** 2))
