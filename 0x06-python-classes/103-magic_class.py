#!/usr/bin/python3

"""MagicClass program"""

import math


class MagicClass:
    """Create a class called MagicClass"""
    def __init__(self, radius=0):
        """Constructor method __init___"""
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Return the area of a circle"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Return the circumference of a circle"""
        return (2 * math.pi * self.__radius)
