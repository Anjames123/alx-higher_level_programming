#!/usr/bin/python3
"""
Module that defines a class MyList that inherits from list
"""


class MyList(list):
    """
    A class MyList that inherits from list
    """

    def __str__(self):
        """
        Return a string representation of the list.
        """
        return str(list(self))

    def print_sorted(self):
        """
        Public instance method that prints the list, but sorted
        (ascending sort)
        """
        print(sorted(self))
