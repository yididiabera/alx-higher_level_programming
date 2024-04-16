#!/usr/bin/python3
"""Serializing an object and storing it in a file"""
import json

def save_to_json_file(my_obj, filename):
    """Moudle to serializes an object and stores it in a file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
