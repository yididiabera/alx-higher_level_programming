#!/usr/bin/python3
"""defines a function to appending to a file"""

def append_write(filename="", text=""):
    """Appends string to a file"""
    count = 0
    with open(filename, "a", encoding="utf-8") as f:
        count = f.write(text)
    return count
