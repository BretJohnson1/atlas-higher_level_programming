#!/usr/bin/python3
""" This module defines a function that checks if classes are identical"""


def is_same_class(obj, a_class):
    """ This function checks if a class is identical to another"""
    return (type(obj) is a_class)
