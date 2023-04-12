#!/usr/bin/python3
"""This module loads an object from a JSON file."""

import json

def load_from_json_file(filename):
    """
    Loads an object from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        The deserialized object.
    """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
