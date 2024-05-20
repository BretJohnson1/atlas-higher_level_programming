#!/usr/bin/python3
""" This module defines a class name BaseGeometry"""


class BaseGeometry:
    """ This defines a class named BaseGeometry"""
    def area(self):
        """ public instance method that calculates area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ public instance method that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
