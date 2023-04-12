#!/usr/bin/python3
"""
Inherits from list
"""


class MyList(list):
    """
    A custom class MyList that inherits from the built-in list class in Python.
    """

    def print_sorted(self):
        """
        Public instance method that sorts and prints the list in ascending
        order.
        """
        sorted_list = sorted(self)  # sort the list in ascending order
        print(sorted_list)  # print the sorted list
