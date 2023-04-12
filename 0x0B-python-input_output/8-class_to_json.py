#!/usr/bin/python3
"""
This module contains a function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean) for JSON
serialization of an object.
"""


def class_to_json(obj):
    """
    Returns a dictionary description with simple data structure for JSON
    serialization of an object.

    Args:
        obj: The object to be serialized.

    Returns:
        A dictionary with simple data structure for JSON serialization.
    """
    return obj.__dict__
