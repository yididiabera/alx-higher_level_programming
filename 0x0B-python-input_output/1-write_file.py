#!/usr/bin/python3
"""For writing a string to a file"""


def write_file(filename="", text=""):
    """module to write to a file"""
    count = 0
    with open(filename, "w", encoding="utf-8") as f:
        count = f.write(text)
    return count
