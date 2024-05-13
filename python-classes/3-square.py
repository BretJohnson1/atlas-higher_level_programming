#!/usr/bin/python3
""" For my square """

class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        """This function defines a square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates area of a square"""
        return (self.__size**2)
