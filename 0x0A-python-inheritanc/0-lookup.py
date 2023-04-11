#!/usr/bin/python3

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    """
    attributes = []
    methods = []
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)
        else:
            attributes.append(attr)
            return sorted(attributes) + sorted(methods)
