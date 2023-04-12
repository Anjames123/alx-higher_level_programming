#!/usr/bin/python3
""" Function that adds a new attribute to an object if it’s possible: """


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to add the attribute to.
        attr: The name of the attribute to add.
        value: The value to assign to the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not isinstance(obj, object):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
