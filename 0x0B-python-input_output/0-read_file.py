#!/usr/bin/python3
"""module to read a text file"""


def read_file(filename=""):
    """
    This function reads a text file (UTF-8) and prints its content to stdout.
    """
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        print(content)
