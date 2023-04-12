#!/usr/bin/python3
"""Save an object to a text file using
a JSON representation."""

import json


def save_to_json_file(my_obj, filename):
    """
    Save an object to a text file using a JSON representation.

    Args:
        my_obj (object): The object to save.
        filename (str): The path to the file.

    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
