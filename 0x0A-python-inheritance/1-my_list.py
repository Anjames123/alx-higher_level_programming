#!/usr/bin/python3
"""
Module that defines a class MyList that inherits from list
"""


class MyList(list):
    """
    A class MyList that inherits from list
    """

    """  Check if all elements in the list are of type int """
    if not all(isinstance(x, int) for x in self):
        print(self)
        return

    def print_sorted(self):
        """
        Public instance method that prints the list, but sorted
        (ascending sort)
        """
        print(sorted(self))
