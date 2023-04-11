#!/usr/bin/python3
""" A class BaseGeometry that serves as a base class for geometry shapes """


class BaseGeometry:
    """
    A class BaseGeometry that serves as a base class for geometry shapes
    """

    def area(self):
        """
        Raises an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a given integer value
        :param name: string representing the name of the integer value
        :param value: integer value to validate
        :raises TypeError: if value is not an integer
        :raises ValueError: if value is less or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
