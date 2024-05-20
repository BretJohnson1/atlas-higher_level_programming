#!/usr/bin/python3
"""
This module defines a function that returns an object
that is represented by a JSON string
"""
import json


def from_json_string(my_str):
    """This function returns an object represented by a JSON string"""
    json_obj = json.loads(my_str)
    return json_obj
