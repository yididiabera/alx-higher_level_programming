#!/usr/bin/python3
"""Defines a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """Creating a Python object from a JSON file"""
    my_obj = None
    data = None
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    my_obj = data
    return my_obj
