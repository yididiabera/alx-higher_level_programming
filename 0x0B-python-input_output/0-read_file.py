#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """reads a file"""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
