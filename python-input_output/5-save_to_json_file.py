#!/usr/bin/python3
"""this is a file to write other json"""
import json


def save_to_json_file(my_obj, filename):
    """this is a function to append to a json"""
    with open(filename, mode='w', encoding="utf-8") as f:
        json.dump(my_obj, f)
