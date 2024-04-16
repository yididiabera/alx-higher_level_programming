#!/usr/bin/python3
"""a function that returns all attributes of an object"""


def class_to_json(obj):
    """module that returns all attributes of an object"""
    my_dict = obj.__dict__
    return my_dict
