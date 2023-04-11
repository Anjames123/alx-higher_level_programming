#!/usr/bin/python3

def lookup(obj):
    """
    Returns a sorted list of all the attributes and methods of an object.

    Parameters:
    obj (object): The object to inspect.

    Returns:
    A list of strings representing the names of all the attributes and methods of the object, sorted in alphabetical order.

    """
    return (dir(obj))
