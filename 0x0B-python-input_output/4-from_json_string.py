#!/usr/bin/python3
"""Deserializing an object"""
import json


def from_json_string(my_str):
    """A module that deserializes an object"""
    return json.loads(my_str)
