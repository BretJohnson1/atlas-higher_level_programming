#!/usr/bin/python3
"""
Ractangle. Building the bas class
"""
from models.base import Base


class Rectangle(Base):
    """ This is a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return (self.__width)

    @property
    def height(self):
        return (self.__height)

    @property
    def x(self):
        return (self.__x)

    @property
    def y(self):
        return (self.__y)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Area function for rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """ Function to display the rectangle"""
        print("\n" * self.y, end='')
        for row in range(self.height):
            print(" " * self.x, end='')
            for col in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ Documentation?"""
        args_len = len(args)
        if args_len >= 1:
            self.id = args[0]
        if args_len >= 2:
            self.width = args[1]
        if args_len >= 3:
            self.height = args[2]
        if args_len >= 4:
            self.x = args[3]
        if args_len >= 5:
            self.y = args[4]

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the rectangle in dictionary form"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
        }
