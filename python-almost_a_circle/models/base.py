#!/usr/bin/python3
""" This class wil be the base of all other classes in this project"""
import json


class Base:
    """ This is the base class"""
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id  # assign id if provided
        else:
            Base.__nb_objects += 1  # if id is not provided
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Function to make into json file"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Function to write json str to file"""
        if list_objs is None:
            list_objs = []

        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as f:
            list = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(list)
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ Returns list of json string data"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Return an instance with all attributes set"""
        if cls.__name__ == 'Rectangle':
            temp = cls(1, 1)
        elif cls.__name__ == 'Square':
            temp = cls(1)

        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """ Returns a list of insrances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                list = cls.from_json_string(f.read())
                return [cls.create(**dictionary) for dictionary in list]
        except FileNotFoundError:
            return []
