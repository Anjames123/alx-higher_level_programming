#!/usr/bin/python3


class MyList(list):
    """
    A custom class MyList that inherits from the built-in list class in Python.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list in ascending order.
        """
        print(sorted(self))

