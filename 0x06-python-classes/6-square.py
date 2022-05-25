#!/usr/bin/python3

"""class Square that defines a square"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """__init__ constructor method: creates a square object.
        args: size - size of the square.
        position - position of the square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position[0]) != int or type(position[1]) \
                != int or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        """Return the square area"""
        return (self.__size ** 2)

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.__size > 0:
            if self.__position[1] > 0:
                print()
            i = 0
            while i < self.__size:
                x = 0
                while x < self.__position[0]:
                    print(" ", end="")
                    x += 1
                y = 0
                while y < self.__size:
                    print("#", end="")
                    y += 1
                print()
                i += 1
        else:
            print()

    @property
    def size(self):
        """Retrieve the square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the square size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the square position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set the square position"""
        if type(value[0]) != int or type(value[1]) \
                != int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
