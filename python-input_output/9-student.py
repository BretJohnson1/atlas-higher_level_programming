#!/usr/bin/python3
"""This module defines a class named Student"""


class Student:
    """This is a class that defines a Student"""

    def __init__(self, first_name, last_name, age):
        """public instantination method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This method returns the dictionary representation"""
        return vars(self)
