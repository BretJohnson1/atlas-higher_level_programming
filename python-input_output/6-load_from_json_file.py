#!/usr/bin/python3
"""This module defines a function that creates an object from JSON file"""
import json


def load_from_json_file(filename):
    """This function creates an object from a JSON file"""
    with open(filename, mode='r', encoding="utf-8") as f:
        return json.load(f)
