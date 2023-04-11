#!/usr/bin/python3
""" Define an attribute lookup function """


def lookup(obj):
    """
    Returns a sorted list of all the attributes and methods of an object.
    """
    return (dir(obj))
