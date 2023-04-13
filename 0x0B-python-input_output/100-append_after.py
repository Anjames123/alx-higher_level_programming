#!/usr/bin/python3
"""Inserts a line of text to a file after each
line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after
    each line containing a specific string.

    Parameters:
    filename (str): The name of the file to modify.
    search_string (str): The string to search for in each line of the file.
    new_string (str): The line of text to insert after
    each line containing the search string.

    Returns:
    None
    """
    with open(filename, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.truncate()
