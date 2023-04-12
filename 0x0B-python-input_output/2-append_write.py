#!/usr/bin/python3
"""This module appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8)
    and returns the number of characters added.

    Args:
        filename (str): The path to the text file. Defaults to an empty string.
        text (str): The string to append to the file. Defaults to an empty string.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode="a+", encoding="utf-8") as f:
        return f.write(text)
