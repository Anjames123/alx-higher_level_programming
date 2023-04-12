#!/usr/bin/python3
"""Returns JSON representation of an object (string)."""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args:
        my_obj (object): The object to be converted to a JSON string.

    Returns:
        str: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
