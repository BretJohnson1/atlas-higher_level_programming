#!/usr/bin/python3
"""My class"""


class Square:
    """Square"""
    def __init__(self, size=0, position=(0, 0)):
        """My private size"""
        self.__size = size
        self.position = position

    @property
    def size(self):
        """My getter """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                [print("#", end="") for j in range(self.__size)]
                print("")
