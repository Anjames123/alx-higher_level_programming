#!/usr/bin/python3
"""check if object if instance of a class that
inherited from specified class"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
