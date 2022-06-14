#!/usr/bin/python3

"""Class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Define the class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ constructor method"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method"""
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method"""
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """x getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter method"""
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter method"""
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, name, value):
        """Validator method"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if name in ["width", "height"] and value <= 0:
            raise ValueError(f"{name} must be > 0")
        if name in ["x", "y"] and value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """Method that returns the area value of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Method that prints in stdout the Rectangle with the character #"""
        print(self.__y * "\n", end="")
        for line in range(self.__height):
            print(self.__x * " ", end="")
            print(self.__width * "#")

    def __str__(self):
        """Method that returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        id = str(self.id)
        x = str(self.__x)
        y = str(self.__y)
        w = str(self.__width)
        h = str(self.__height)
        return "[Rectangle] (" + id + ") " + x + "/" + y + " - " + w + "/" + h

    def update(self, *args, **kwargs):
        """Method that assigns an argument to each attribute"""
        if args and len(args) > 0:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.width = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
            if len(args) == 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Method that returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
