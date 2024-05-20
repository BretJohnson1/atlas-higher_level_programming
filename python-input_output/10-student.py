#!/usr/bin/python3
"""This module defines a class named Student"""


class Student:
    """This is a class that defines a Student"""

    def __init__(self, first_name, last_name, age):
        """public instantination method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This method returns the dictionary representation"""
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
                }
        return self.__dict__
