#!/usr/bin/python3
"""
This is for a square and not a circle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This is a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width or self.height))

    def update(self, *args, **kwargs):
        """ Documentation?"""
        if args and len(args) > 0:
            attributes = ['id', 'size', "x", "y"]
            for index, arg in enumerate(args):
                if index < len(attributes):
                    if attributes[index] == "size":
                        self.width = arg
                        self.height = arg
                    else:
                        setattr(self, attributes[index], arg)
        else:
            for key, arg in kwargs.items():
                if hasattr(self, key):
                    if key == "size":
                        self.width = arg
                        self.height = arg
                    else:
                        setattr(self, key, arg)

    def to_dictionary(self):
        """ Returns the square in dictionary form"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y,
        }
