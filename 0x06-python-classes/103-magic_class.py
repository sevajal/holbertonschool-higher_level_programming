#!/usr/bin/python3
class MagicClass:
    def __init__(self, radius):
        if radius is not int or radius is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return ((self.__radius ** 2) * math(pi))

    def circumference(self):
        return (math(pi) * (self.__radius ** 2))
