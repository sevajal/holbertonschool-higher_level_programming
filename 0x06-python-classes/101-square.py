#!/usr/bin/python3

"""class Square that defines a square"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """__init__ constructor method: creates a square object.
        args: size - size of the square.
        position - position of the square"""
        self.size = size
        self.position = position

    def area(self):
        """Return the square area"""
        return (self.__size ** 2)

    def my_print(self):
        """ prints in stdout the square with the character #"""
        size = self.__size
        if size > 0:
            print(self.__position[1] * "\n", end="")
            [print(self.__position[0] * " " + size * "#") for i in range(size)]
        else:
            print()

    def __str__(self):
        """Prints the square as a string"""
        result = ""
        size = self.__size
        if size > 0:
            result += self.__position[1] * "\n"
            for i in range(size - 1):
                result += self.__position[0] * " " + size * "#" + "\n"
            result += self.__position[0] * " " + size * "#"
            return (result)
        else:
            return (result)

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
        if type(value) != tuple or len(value) != 2 \
                or type(value[0]) != int or type(value[1]) != int \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
