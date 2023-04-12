#!/usr/bin/env python3

def read_file(filename=""):
    """
    This function reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The path to the text file. Defaults to an empty string.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        print(content)
