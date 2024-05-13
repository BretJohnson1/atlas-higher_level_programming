#!/usr/bin/python3
"""For my square"""


class Square:
    """ Initializing Class for my square."""
    def __init__(self, size=0):
        """ New sqaure


        Args:
        size (int): Size of square"""
        self.__size = size

    @property
    def size(self):
        """Getter """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Area of sqaure"""
        return (self.__size * self.__size)
