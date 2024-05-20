#!/usr/bin/python3
""" This module defines a function that identifies an objects subclass"""


def inherits_from(obj, a_class):
    """ This function identifies an objects subclass"""
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
