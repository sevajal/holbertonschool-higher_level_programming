#!/usr/bin/python3

"""Class Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__ constructor method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Method that returns [Square] (<id>) <x>/<y> - <size>"""
        id = str(self.id)
        x = str(self.x)
        y = str(self.y)
        size = str(self.width)
        return "[Square] (" + id + ") " + x + "/" + y + " - " + size

    @property
    def size(self):
        """size getter method"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter method"""
        self.integer_validator("width", value)
        self.width = value
        self.heigth = value

    def update(self, *args, **kwargs):
        """Method that assigns an argument to each attribute"""
        if args and len(args) > 0:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Method that returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
