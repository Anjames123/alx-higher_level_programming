#!/usr/bin/python3
"""Function that returns True if the object is an instance of, or if the object
is an instance of a class that inherited from, the specified class; otherwise False"""


def is_kind_of_class(obj, a_class):
    """
    Determines if obj is an instance of, or if obj is an instance of a class
    that inherited from, the specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to check.

    Returns:
        bool: True if obj is an instance of, or if obj is an instance of a class
        that inherited from, the specified class; otherwise False.
    """
    return isinstance(obj, a_class)
