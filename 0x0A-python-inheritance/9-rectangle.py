#!/usr/bin/python3
"""
Module that defines a class BaseGeometry
"""


class BaseGeometry:
    """
    A class BaseGeometry that is an empty class
    """

    def area(self):
        """
        Public instance method that raises an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value:
        * you can assume name is always a string
        * if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
        * if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height: def __init__(self, width, height):
        width and height must be private. No getter or setter
        width and height must be positive integers validated by integer_validator
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """
        Implements the area() method
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Prints and returns the following rectangle description: [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
