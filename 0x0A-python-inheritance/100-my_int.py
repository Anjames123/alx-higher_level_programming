#!/usr/bin/python3
""" Define A class MyInt that inherits from int and inverts the ==
and != operators """


class MyInt(int):
    """
    A class MyInt that inherits from int and inverts the == and != operators
    """
    def __eq__(self, other):
        """
        Inverts the == operator
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator
        """
        return super().__eq__(other)
